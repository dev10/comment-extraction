# Generated from RustComment.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\6\2\23\n\2\r\2\16\2\24\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\7\3\35\n\3\f\3\16\3 \13\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\7\5(\n\5\f\5\16\5+\13\5\3\5\3\5\3\6\3\6\7\6\61\n\6")
        buf.write("\f\6\16\6\64\13\6\3\7\7\7\67\n\7\f\7\16\7:\13\7\3\7\4")
        buf.write("\628\2\b\2\4\6\b\n\f\2\4\3\2\3\3\3\2\4\4\2:\2\16\3\2\2")
        buf.write("\2\4\26\3\2\2\2\6!\3\2\2\2\b$\3\2\2\2\n.\3\2\2\2\f8\3")
        buf.write("\2\2\2\16\22\5\f\7\2\17\20\5\4\3\2\20\21\5\n\6\2\21\23")
        buf.write("\3\2\2\2\22\17\3\2\2\2\23\24\3\2\2\2\24\22\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25\3\3\2\2\2\26\27\7\n\2\2\27\30\5\6\4\2\30")
        buf.write("\36\5\b\5\2\31\32\5\f\7\2\32\33\5\4\3\2\33\35\3\2\2\2")
        buf.write("\34\31\3\2\2\2\35 \3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2")
        buf.write("\37\5\3\2\2\2 \36\3\2\2\2!\"\7\7\2\2\"#\7\n\2\2#\7\3\2")
        buf.write("\2\2$)\7\t\2\2%&\7\n\2\2&(\7\t\2\2\'%\3\2\2\2(+\3\2\2")
        buf.write("\2)\'\3\2\2\2)*\3\2\2\2*,\3\2\2\2+)\3\2\2\2,-\7\b\2\2")
        buf.write("-\t\3\2\2\2.\62\7\b\2\2/\61\n\2\2\2\60/\3\2\2\2\61\64")
        buf.write("\3\2\2\2\62\63\3\2\2\2\62\60\3\2\2\2\63\13\3\2\2\2\64")
        buf.write("\62\3\2\2\2\65\67\n\3\2\2\66\65\3\2\2\2\67:\3\2\2\289")
        buf.write("\3\2\2\28\66\3\2\2\29\r\3\2\2\2:8\3\2\2\2\7\24\36)\62")
        buf.write("8")
        return buf.getvalue()


class RustCommentParser ( Parser ):

    grammarFileName = "RustComment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n//'", "'/**'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "WS", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "END_SYMBOL", "TEXT", "NL", "IGNORED_ALPHA", 
                      "IGNORED_SYMBOLS" ]

    RULE_sourceFile = 0
    RULE_comment = 1
    RULE_blockComment = 2
    RULE_codeDeclaration = 3
    RULE_ignored = 4
    RULE_ignoredPreamble = 5

    ruleNames =  [ "sourceFile", "comment", "blockComment", "codeDeclaration", 
                   "ignored", "ignoredPreamble" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    WS=3
    LINE_COMMENT=4
    BLOCK_COMMENT=5
    END_SYMBOL=6
    TEXT=7
    NL=8
    IGNORED_ALPHA=9
    IGNORED_SYMBOLS=10

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
            return self.getTypedRuleContext(RustCommentParser.IgnoredPreambleContext,0)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RustCommentParser.CommentContext)
            else:
                return self.getTypedRuleContext(RustCommentParser.CommentContext,i)


        def ignored(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RustCommentParser.IgnoredContext)
            else:
                return self.getTypedRuleContext(RustCommentParser.IgnoredContext,i)


        def getRuleIndex(self):
            return RustCommentParser.RULE_sourceFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceFile" ):
                listener.enterSourceFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceFile" ):
                listener.exitSourceFile(self)




    def sourceFile(self):

        localctx = RustCommentParser.SourceFileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sourceFile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.ignoredPreamble()
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 13
                self.comment()
                self.state = 14
                self.ignored()
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==RustCommentParser.NL):
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

        def NL(self):
            return self.getToken(RustCommentParser.NL, 0)

        def blockComment(self):
            return self.getTypedRuleContext(RustCommentParser.BlockCommentContext,0)


        def codeDeclaration(self):
            return self.getTypedRuleContext(RustCommentParser.CodeDeclarationContext,0)


        def ignoredPreamble(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RustCommentParser.IgnoredPreambleContext)
            else:
                return self.getTypedRuleContext(RustCommentParser.IgnoredPreambleContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RustCommentParser.CommentContext)
            else:
                return self.getTypedRuleContext(RustCommentParser.CommentContext,i)


        def getRuleIndex(self):
            return RustCommentParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = RustCommentParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(RustCommentParser.NL)
            self.state = 21
            self.blockComment()
            self.state = 22
            self.codeDeclaration()
            self.state = 28
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 23
                    self.ignoredPreamble()
                    self.state = 24
                    self.comment() 
                self.state = 30
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
            return self.getToken(RustCommentParser.BLOCK_COMMENT, 0)

        def NL(self):
            return self.getToken(RustCommentParser.NL, 0)

        def getRuleIndex(self):
            return RustCommentParser.RULE_blockComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockComment" ):
                listener.enterBlockComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockComment" ):
                listener.exitBlockComment(self)




    def blockComment(self):

        localctx = RustCommentParser.BlockCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_blockComment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(RustCommentParser.BLOCK_COMMENT)
            self.state = 32
            self.match(RustCommentParser.NL)
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

        def TEXT(self, i:int=None):
            if i is None:
                return self.getTokens(RustCommentParser.TEXT)
            else:
                return self.getToken(RustCommentParser.TEXT, i)

        def END_SYMBOL(self):
            return self.getToken(RustCommentParser.END_SYMBOL, 0)

        def NL(self, i:int=None):
            if i is None:
                return self.getTokens(RustCommentParser.NL)
            else:
                return self.getToken(RustCommentParser.NL, i)

        def getRuleIndex(self):
            return RustCommentParser.RULE_codeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeDeclaration" ):
                listener.enterCodeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeDeclaration" ):
                listener.exitCodeDeclaration(self)




    def codeDeclaration(self):

        localctx = RustCommentParser.CodeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_codeDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(RustCommentParser.TEXT)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==RustCommentParser.NL:
                self.state = 35
                self.match(RustCommentParser.NL)
                self.state = 36
                self.match(RustCommentParser.TEXT)
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 42
            self.match(RustCommentParser.END_SYMBOL)
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

        def END_SYMBOL(self):
            return self.getToken(RustCommentParser.END_SYMBOL, 0)

        def getRuleIndex(self):
            return RustCommentParser.RULE_ignored

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnored" ):
                listener.enterIgnored(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnored" ):
                listener.exitIgnored(self)




    def ignored(self):

        localctx = RustCommentParser.IgnoredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ignored)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(RustCommentParser.END_SYMBOL)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 45
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==RustCommentParser.T__0:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 50
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
            return RustCommentParser.RULE_ignoredPreamble

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnoredPreamble" ):
                listener.enterIgnoredPreamble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnoredPreamble" ):
                listener.exitIgnoredPreamble(self)




    def ignoredPreamble(self):

        localctx = RustCommentParser.IgnoredPreambleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ignoredPreamble)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 51
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==RustCommentParser.T__1:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





