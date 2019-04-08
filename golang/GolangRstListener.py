from common.listener import CommonRstListener
from golang.GolangCommentParser import GolangCommentParser
from golang.GolangCommentListener import GolangCommentListener


class GolangRstListener(GolangCommentListener, CommonRstListener):
    def __init__(self, stripped_file_name, output, url):
        CommonRstListener.__init__(self, stripped_file_name, output, url)

    def enterSourceFile(self, ctx: GolangCommentParser.SourceFileContext):
        CommonRstListener.enter_source_file(self, ctx)

    def exitSourceFile(self, ctx: GolangCommentParser.SourceFileContext):
        CommonRstListener.exit_source_file(self, ctx)

    def enterComment(self, ctx: GolangCommentParser.CommentContext):
        CommonRstListener.enter_comment(self, ctx)

    def exitComment(self, ctx: GolangCommentParser.CommentContext):
        CommonRstListener.exit_comment(self, ctx, strip_line_comments=True, strip_block_comments=True)
