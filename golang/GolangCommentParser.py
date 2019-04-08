# Generated from GolangComment.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\13")
        buf.write("E\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\6\2\25\n\2\r\2\16\2\26\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\37\n\3\3\4\3\4\7\4#\n\4\f\4\16\4&\13")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\7\7\62\n\7")
        buf.write("\f\7\16\7\65\13\7\3\b\7\b8\n\b\f\b\16\b;\13\b\3\b\7\b")
        buf.write(">\n\b\f\b\16\bA\13\b\5\bC\n\b\3\b\6$\639?\2\t\2\4\6\b")
        buf.write("\n\f\16\2\5\3\2\4\4\3\2\6\6\3\2\7\7\2D\2\20\3\2\2\2\4")
        buf.write("\36\3\2\2\2\6 \3\2\2\2\b)\3\2\2\2\n-\3\2\2\2\f/\3\2\2")
        buf.write("\2\16B\3\2\2\2\20\24\5\16\b\2\21\22\5\4\3\2\22\23\5\f")
        buf.write("\7\2\23\25\3\2\2\2\24\21\3\2\2\2\25\26\3\2\2\2\26\24\3")
        buf.write("\2\2\2\26\27\3\2\2\2\27\3\3\2\2\2\30\31\5\6\4\2\31\32")
        buf.write("\5\n\6\2\32\37\3\2\2\2\33\34\5\b\5\2\34\35\5\n\6\2\35")
        buf.write("\37\3\2\2\2\36\30\3\2\2\2\36\33\3\2\2\2\37\5\3\2\2\2 ")
        buf.write("$\7\3\2\2!#\n\2\2\2\"!\3\2\2\2#&\3\2\2\2$%\3\2\2\2$\"")
        buf.write("\3\2\2\2%\'\3\2\2\2&$\3\2\2\2\'(\7\4\2\2(\7\3\2\2\2)*")
        buf.write("\7\4\2\2*+\7\b\2\2+,\7\4\2\2,\t\3\2\2\2-.\7\t\2\2.\13")
        buf.write("\3\2\2\2/\63\7\5\2\2\60\62\n\3\2\2\61\60\3\2\2\2\62\65")
        buf.write("\3\2\2\2\63\64\3\2\2\2\63\61\3\2\2\2\64\r\3\2\2\2\65\63")
        buf.write("\3\2\2\2\668\n\3\2\2\67\66\3\2\2\28;\3\2\2\29:\3\2\2\2")
        buf.write("9\67\3\2\2\2:C\3\2\2\2;9\3\2\2\2<>\n\4\2\2=<\3\2\2\2>")
        buf.write("A\3\2\2\2?@\3\2\2\2?=\3\2\2\2@C\3\2\2\2A?\3\2\2\2B9\3")
        buf.write("\2\2\2B?\3\2\2\2C\17\3\2\2\2\t\26\36$\639?B")
        return buf.getvalue()


class GolangCommentParser ( Parser ):

    grammarFileName = "GolangComment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n// '", "'\n'", "'{'", "'\n//'", "'*/\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BLOCK_COMMENT", "TEXT", 
                      "NL", "IGNORED" ]

    RULE_sourceFile = 0
    RULE_comment = 1
    RULE_lineComment = 2
    RULE_blockComment = 3
    RULE_codeDeclaration = 4
    RULE_ignored = 5
    RULE_ignoredPreamble = 6

    ruleNames =  [ "sourceFile", "comment", "lineComment", "blockComment", 
                   "codeDeclaration", "ignored", "ignoredPreamble" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    BLOCK_COMMENT=6
    TEXT=7
    NL=8
    IGNORED=9

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SourceFileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ignoredPreamble(self):
            return self.getTypedRuleContext(GolangCommentParser.IgnoredPreambleContext,0)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GolangCommentParser.CommentContext)
            else:
                return self.getTypedRuleContext(GolangCommentParser.CommentContext,i)


        def ignored(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GolangCommentParser.IgnoredContext)
            else:
                return self.getTypedRuleContext(GolangCommentParser.IgnoredContext,i)


        def getRuleIndex(self):
            return GolangCommentParser.RULE_sourceFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceFile" ):
                listener.enterSourceFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceFile" ):
                listener.exitSourceFile(self)




    def sourceFile(self):

        localctx = GolangCommentParser.SourceFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.ignoredPreamble()
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 15
                self.comment()
                self.state = 16
                self.ignored()
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==GolangCommentParser.T__0 or _la==GolangCommentParser.T__1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lineComment(self):
            return self.getTypedRuleContext(GolangCommentParser.LineCommentContext,0)


        def codeDeclaration(self):
            return self.getTypedRuleContext(GolangCommentParser.CodeDeclarationContext,0)


        def blockComment(self):
            return self.getTypedRuleContext(GolangCommentParser.BlockCommentContext,0)


        def getRuleIndex(self):
            return GolangCommentParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = GolangCommentParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GolangCommentParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.lineComment()
                self.state = 23
                self.codeDeclaration()
                pass
            elif token in [GolangCommentParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.blockComment()
                self.state = 26
                self.codeDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineCommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GolangCommentParser.RULE_lineComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineComment" ):
                listener.enterLineComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineComment" ):
                listener.exitLineComment(self)




    def lineComment(self):

        localctx = GolangCommentParser.LineCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lineComment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(GolangCommentParser.T__0)
            self.state = 34
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 31
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==GolangCommentParser.T__1:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 36
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 37
            self.match(GolangCommentParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockCommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_COMMENT(self):
            return self.getToken(GolangCommentParser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return GolangCommentParser.RULE_blockComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockComment" ):
                listener.enterBlockComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockComment" ):
                listener.exitBlockComment(self)




    def blockComment(self):

        localctx = GolangCommentParser.BlockCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_blockComment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(GolangCommentParser.T__1)
            self.state = 40
            self.match(GolangCommentParser.BLOCK_COMMENT)
            self.state = 41
            self.match(GolangCommentParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CodeDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXT(self):
            return self.getToken(GolangCommentParser.TEXT, 0)

        def getRuleIndex(self):
            return GolangCommentParser.RULE_codeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeDeclaration" ):
                listener.enterCodeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeDeclaration" ):
                listener.exitCodeDeclaration(self)




    def codeDeclaration(self):

        localctx = GolangCommentParser.CodeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_codeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(GolangCommentParser.TEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoredContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GolangCommentParser.RULE_ignored

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnored" ):
                listener.enterIgnored(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnored" ):
                listener.exitIgnored(self)




    def ignored(self):

        localctx = GolangCommentParser.IgnoredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ignored)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(GolangCommentParser.T__2)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 46
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==GolangCommentParser.T__3:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IgnoredPreambleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GolangCommentParser.RULE_ignoredPreamble

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnoredPreamble" ):
                listener.enterIgnoredPreamble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnoredPreamble" ):
                listener.exitIgnoredPreamble(self)




    def ignoredPreamble(self):

        localctx = GolangCommentParser.IgnoredPreambleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ignoredPreamble)
        self._la = 0 # Token type
        try:
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 52
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==GolangCommentParser.T__3:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 57
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 58
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==GolangCommentParser.T__4:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 63
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





