# Generated from GolangComment.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GolangCommentParser import GolangCommentParser
else:
    from GolangCommentParser import GolangCommentParser

# This class defines a complete listener for a parse tree produced by GolangCommentParser.
class GolangCommentListener(ParseTreeListener):

    # Enter a parse tree produced by GolangCommentParser#sourceFile.
    def enterSourceFile(self, ctx:GolangCommentParser.SourceFileContext):
        pass

    # Exit a parse tree produced by GolangCommentParser#sourceFile.
    def exitSourceFile(self, ctx:GolangCommentParser.SourceFileContext):
        pass


    # Enter a parse tree produced by GolangCommentParser#comment.
    def enterComment(self, ctx:GolangCommentParser.CommentContext):
        pass

    # Exit a parse tree produced by GolangCommentParser#comment.
    def exitComment(self, ctx:GolangCommentParser.CommentContext):
        pass


    # Enter a parse tree produced by GolangCommentParser#lineComment.
    def enterLineComment(self, ctx:GolangCommentParser.LineCommentContext):
        pass

    # Exit a parse tree produced by GolangCommentParser#lineComment.
    def exitLineComment(self, ctx:GolangCommentParser.LineCommentContext):
        pass


    # Enter a parse tree produced by GolangCommentParser#blockComment.
    def enterBlockComment(self, ctx:GolangCommentParser.BlockCommentContext):
        pass

    # Exit a parse tree produced by GolangCommentParser#blockComment.
    def exitBlockComment(self, ctx:GolangCommentParser.BlockCommentContext):
        pass


    # Enter a parse tree produced by GolangCommentParser#codeDeclaration.
    def enterCodeDeclaration(self, ctx:GolangCommentParser.CodeDeclarationContext):
        pass

    # Exit a parse tree produced by GolangCommentParser#codeDeclaration.
    def exitCodeDeclaration(self, ctx:GolangCommentParser.CodeDeclarationContext):
        pass


    # Enter a parse tree produced by GolangCommentParser#ignored.
    def enterIgnored(self, ctx:GolangCommentParser.IgnoredContext):
        pass

    # Exit a parse tree produced by GolangCommentParser#ignored.
    def exitIgnored(self, ctx:GolangCommentParser.IgnoredContext):
        pass


    # Enter a parse tree produced by GolangCommentParser#ignoredPreamble.
    def enterIgnoredPreamble(self, ctx:GolangCommentParser.IgnoredPreambleContext):
        pass

    # Exit a parse tree produced by GolangCommentParser#ignoredPreamble.
    def exitIgnoredPreamble(self, ctx:GolangCommentParser.IgnoredPreambleContext):
        pass


