from common.listener import CommonRstListener
from java.JavaCommentParser import JavaCommentParser
from java.JavaCommentListener import JavaCommentListener


class JavaRstListener(JavaCommentListener, CommonRstListener):
    def __init__(self, stripped_file_name, output, url):
        print('JavaRstListener')
        CommonRstListener.__init__(self, stripped_file_name, output, url)

    def enterSourceFile(self, ctx:JavaCommentParser.SourceFileContext):
        print('enterSourceFile')
        CommonRstListener.enter_source_file(self, ctx)

    def exitSourceFile(self, ctx:JavaCommentParser.SourceFileContext):
        print('exitSourceFile')
        CommonRstListener.exit_source_file(self, ctx)

    def enterComment(self, ctx:JavaCommentParser.CommentContext):
        print('enterComment')
        CommonRstListener.enter_comment(self, ctx)

    def exitComment(self, ctx:JavaCommentParser.CommentContext):
        print('exitComment')
        CommonRstListener.exit_comment(self, ctx, strip_line_comments=False, strip_block_comments=True)
