# Generated from RustComment.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RustCommentParser import RustCommentParser
else:
    from RustCommentParser import RustCommentParser

# This class defines a complete listener for a parse tree produced by RustCommentParser.
class RustCommentListener(ParseTreeListener):

    # Enter a parse tree produced by RustCommentParser#sourceFile.
    def enterSourceFile(self, ctx:RustCommentParser.SourceFileContext):
        pass

    # Exit a parse tree produced by RustCommentParser#sourceFile.
    def exitSourceFile(self, ctx:RustCommentParser.SourceFileContext):
        pass


    # Enter a parse tree produced by RustCommentParser#comment.
    def enterComment(self, ctx:RustCommentParser.CommentContext):
        pass

    # Exit a parse tree produced by RustCommentParser#comment.
    def exitComment(self, ctx:RustCommentParser.CommentContext):
        pass


    # Enter a parse tree produced by RustCommentParser#blockComment.
    def enterBlockComment(self, ctx:RustCommentParser.BlockCommentContext):
        pass

    # Exit a parse tree produced by RustCommentParser#blockComment.
    def exitBlockComment(self, ctx:RustCommentParser.BlockCommentContext):
        pass


    # Enter a parse tree produced by RustCommentParser#codeDeclaration.
    def enterCodeDeclaration(self, ctx:RustCommentParser.CodeDeclarationContext):
        pass

    # Exit a parse tree produced by RustCommentParser#codeDeclaration.
    def exitCodeDeclaration(self, ctx:RustCommentParser.CodeDeclarationContext):
        pass


    # Enter a parse tree produced by RustCommentParser#ignored.
    def enterIgnored(self, ctx:RustCommentParser.IgnoredContext):
        pass

    # Exit a parse tree produced by RustCommentParser#ignored.
    def exitIgnored(self, ctx:RustCommentParser.IgnoredContext):
        pass


    # Enter a parse tree produced by RustCommentParser#ignoredPreamble.
    def enterIgnoredPreamble(self, ctx:RustCommentParser.IgnoredPreambleContext):
        pass

    # Exit a parse tree produced by RustCommentParser#ignoredPreamble.
    def exitIgnoredPreamble(self, ctx:RustCommentParser.IgnoredPreambleContext):
        pass


