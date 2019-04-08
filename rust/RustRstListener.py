from common.listener import CommonRstListener
from rust.RustCommentParser import RustCommentParser
from rust.RustCommentListener import RustCommentListener


class RustRstListener(RustCommentListener, CommonRstListener):
    def __init__(self, stripped_file_name, output, url):
        CommonRstListener.__init__(self, stripped_file_name, output, url)

    def enterSourceFile(self, ctx: RustCommentParser.SourceFileContext):
        CommonRstListener.enter_source_file(self, ctx)

    def exitSourceFile(self, ctx: RustCommentParser.SourceFileContext):
        CommonRstListener.exit_source_file(self, ctx)

    def enterComment(self, ctx: RustCommentParser.CommentContext):
        print('enterComment')

    def exitComment(self, ctx: RustCommentParser.CommentContext):
        CommonRstListener.exit_comment(self, ctx, strip_line_comments=False, strip_block_comments=True)
