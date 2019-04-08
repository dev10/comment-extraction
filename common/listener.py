import re

UNKNOWN_LINE = '???'


class CommonRstListener(object):
    def __init__(self, stripped_file_name, output, url):
        print('CommonRstListener')
        self.buffer = {}
        self.output = output
        self.url = url

        file_url = "`" + str(stripped_file_name) + ' <' + url + '>`_\n'
        file_header = ['*' * len(file_url), '\n', file_url, '*' * len(file_url), '\n']
        self.write_output(-1, file_header)

    def write_output(self, line_number, list_buffer):
        output_line = 0
        if line_number == UNKNOWN_LINE:
            print("Unknown line detected")
        else:
            output_line = int(line_number)

        self.buffer[output_line] = "".join(list_buffer)

    def enter_source_file(self, ctx):
        print('enter_source_file')

    def exit_source_file(self, ctx):
        print('exit_source_file.. writing buffer to rst file')
        for key in sorted(self.buffer):
            print("writing output from line: %d" % key)
            self.output.write(self.buffer[key])

    def enter_comment(self, ctx):
        print('enter_comment')

    def exit_comment(self, ctx, strip_line_comments, strip_block_comments):
        print('exit_comment')

        comments = ''
        if strip_line_comments:
            line_comment = ctx.lineComment()
            if line_comment is not None:
                comments = line_comment.getText().strip().strip('//').split('//')

        if strip_block_comments:
            block_comment = ctx.blockComment()
            if block_comment is not None:
                comments = block_comment.getText().strip().strip('/*').strip('*/').split('\n')

        is_empty = next((False for c in comments if c.strip() != ""), True)
        if is_empty:
            return

        output = ['\n\n.. function:: ']
        code = ctx.codeDeclaration()
        code_text = code.TEXT()

        if code is None:
            return

        cleaned_text = code.getText().replace('\n', ' ').strip()
        cleaned_text = re.sub(r'[ \t]+', ' ', cleaned_text)     # cleanup tabs and spaces
        cleaned_text = re.sub(r'[;{]+$', '', cleaned_text)      # remove line ending symbols
        cleaned_text = cleaned_text.strip()
        output.append(cleaned_text)
        source_line = UNKNOWN_LINE
        if code_text is not None:
            if hasattr(code_text, 'getSymbol'):
                source_line = code_text.getSymbol().line
            elif isinstance(code_text, list) and len(code_text) > 0:    # necessary for Rust grammar
                source_line = code_text[0].getSymbol().line

        output.append(" [line: %s]" % source_line)

        output.append('\n\n')

        preserve_output_with_pipe = True
        has_pipe = next((c for c in comments if c.strip().startswith('|')), False)
        if has_pipe:
            print('output without line break for [%s]' % comments)
            output.append('\t::\n\n')
            preserve_output_with_pipe = False

        preserve_all = False
        has_markup = next((c for c in comments if c.strip().startswith('.. ') and '::' in c), False)
        if has_markup:
            print('output must be preserved for [%s]' % comments)
            preserve_all = True
            preserve_output_with_pipe = False

        for full_comment in comments:
            clean_comment = re.sub(r'^[ \t*]+', '', full_comment)       # remove line starting symbols
            clean_comment = clean_comment.strip()
            if clean_comment != '' or preserve_all:
                if preserve_output_with_pipe:
                    output.append('\t| ' + clean_comment + '\n')
                elif preserve_all:
                    output.append(full_comment + '\n')
                else:
                    output.append('\t\t' + clean_comment + '\n')

        output.append('\n`View source at line: %s <%s#L%s>`_' % (source_line, self.url, source_line))
        self.write_output(source_line, output)
