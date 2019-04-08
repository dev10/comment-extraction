# Generated from JavaComment.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JavaCommentParser import JavaCommentParser
else:
    from JavaCommentParser import JavaCommentParser

# This class defines a complete listener for a parse tree produced by JavaCommentParser.
class JavaCommentListener(ParseTreeListener):

    # Enter a parse tree produced by JavaCommentParser#sourceFile.
    def enterSourceFile(self, ctx:JavaCommentParser.SourceFileContext):
        pass

    # Exit a parse tree produced by JavaCommentParser#sourceFile.
    def exitSourceFile(self, ctx:JavaCommentParser.SourceFileContext):
        pass


    # Enter a parse tree produced by JavaCommentParser#comment.
    def enterComment(self, ctx:JavaCommentParser.CommentContext):
        pass

    # Exit a parse tree produced by JavaCommentParser#comment.
    def exitComment(self, ctx:JavaCommentParser.CommentContext):
        pass


    # Enter a parse tree produced by JavaCommentParser#blockComment.
    def enterBlockComment(self, ctx:JavaCommentParser.BlockCommentContext):
        pass

    # Exit a parse tree produced by JavaCommentParser#blockComment.
    def exitBlockComment(self, ctx:JavaCommentParser.BlockCommentContext):
        pass


    # Enter a parse tree produced by JavaCommentParser#codeDeclaration.
    def enterCodeDeclaration(self, ctx:JavaCommentParser.CodeDeclarationContext):
        pass

    # Exit a parse tree produced by JavaCommentParser#codeDeclaration.
    def exitCodeDeclaration(self, ctx:JavaCommentParser.CodeDeclarationContext):
        pass


    # Enter a parse tree produced by JavaCommentParser#ignored.
    def enterIgnored(self, ctx:JavaCommentParser.IgnoredContext):
        pass

    # Exit a parse tree produced by JavaCommentParser#ignored.
    def exitIgnored(self, ctx:JavaCommentParser.IgnoredContext):
        pass


    # Enter a parse tree produced by JavaCommentParser#ignoredPreamble.
    def enterIgnoredPreamble(self, ctx:JavaCommentParser.IgnoredPreambleContext):
        pass

    # Exit a parse tree produced by JavaCommentParser#ignoredPreamble.
    def exitIgnoredPreamble(self, ctx:JavaCommentParser.IgnoredPreambleContext):
        pass


