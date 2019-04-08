import argparse
import glob
import ntpath
import os
import sys
from antlr4 import *
# Golang parser imports
from golang.GolangCommentLexer import GolangCommentLexer
from golang.GolangCommentParser import GolangCommentParser
from golang.GolangRstListener import GolangRstListener
# Java parser imports
from java.JavaCommentLexer import JavaCommentLexer
from java.JavaCommentParser import JavaCommentParser
from java.JavaRstListener import JavaRstListener
# Rust parser imports
from rust.RustCommentLexer import RustCommentLexer
from rust.RustCommentParser import RustCommentParser
from rust.RustRstListener import RustRstListener

def main(argv):
    parser = argparse.ArgumentParser(description='generate rst files from source comments')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', help='input source file')
    group.add_argument('-d', '--directory', help='input source directory')
    parser.add_argument('-o','--output', help='the output directory', required=True)
    parser.add_argument('-l', '--language',
                        required=True,
                        help='select programming language to parse',
                        choices=['golang', 'java', 'rust'])
    parser.add_argument('-sp', '--strip-prefix',
                        help='path to strip from input for link generation, eg /home/user/tmp/go-lachesis')
    parser.add_argument('-ru', '--repo-url', required=True,
                        help='github repo url for link generation, eg https://github.com/Fantom-foundation/go-lachesis')
    parser.add_argument('-ct', '--commit-tag', required=True,
                        help='github commit tag / branch / id for link generation eg master')

    args = parser.parse_args()

    if args.strip_prefix is None:
        print('not stripping prefix')

    # process args
    if args.file:
        extract_from_file(args.file, args)
    elif args.directory:
        extract_from_directory(args.directory, args)
    else:
        print('file or directory input required')
        return


def extract_from_file(file, args):
    print('input file [%s]' % file)

    lang_parser = None
    if args.language == 'golang':
        print('using golang antlr parser')
        lang_parser = {'lexer': GolangCommentLexer,
                  'parser': GolangCommentParser,
                  'listener': GolangRstListener}
    elif args.language == 'java':
        print('using java antlr parser')
        lang_parser = {'lexer': JavaCommentLexer,
                  'parser': JavaCommentParser,
                  'listener': JavaRstListener}
    elif args.language == 'rust':
        print('using rust antlr parser')
        lang_parser = {'lexer': RustCommentLexer,
                  'parser': RustCommentParser,
                  'listener': RustRstListener}
    else:
        print('unsupported language [%s]' % args.language)
        return

    # return
    input_filepath = file
    in_file = FileStream(input_filepath)
    lexer = lang_parser['lexer'](in_file)
    stream = CommonTokenStream(lexer)
    parser = lang_parser['parser'](stream)

    tree = parser.sourceFile()
    new_file_name = get_new_filename(input_filepath, args.output)
    output = open(new_file_name, 'w')

    # rst = JavaRstListener(input_filepath, output)
    clean_file_path = strip_path_prefix(input_filepath, args.strip_prefix)
    url = create_github_file_url(clean_file_path, args.repo_url, args.commit_tag)
    rst = lang_parser['listener'](clean_file_path, output, url)
    walker = ParseTreeWalker()
    print('sourceFile: ', tree)
    walker.walk(rst, tree)

    output.close()


def create_github_file_url(clean_file_path, repo_base_url, commit_tag):
    # clean file path example: /src/test/java/poset/PosetTest.java
    # repo base url example: https://github.com/Fantom-Foundation/jlachesis
    # commit tag example: master
    # example output: https://github.com/Fantom-Foundation/jlachesis/blob/master/src/test/java/poset/PosetTest.java

    url = repo_base_url + '/blob/' + commit_tag + clean_file_path
    print('setting file url to: ' + url)
    return url


def extract_from_directory(directory, args):
    print('input directory [%s]' % directory)

    lang = args.language
    glob_path = ''
    if lang == 'golang':
        glob_path = '/**/*.go'
    elif lang == 'java':
        glob_path = '/**/*.java'
    elif lang == 'rust':
        glob_path = '/**/*.rs'

    glob_path = directory + glob_path
    print('extracting comments that match glob [%s]' % glob_path)
    for filename in glob.iglob(glob_path, recursive=True):
        extract_from_file(filename, args)


def get_new_filename(original, output, extension='.rst'):
    new = ntpath.basename(original)
    if new == '':
        raise Exception('invalid file path given: ' + original)
    return os.path.join(output, new) + extension


def strip_path_prefix(file_path, strip_prefix):
    if strip_prefix and file_path.startswith(strip_prefix):
        file_path = file_path.replace(strip_prefix, '', 1)

    return file_path


if __name__ == '__main__':
    main(sys.argv)
