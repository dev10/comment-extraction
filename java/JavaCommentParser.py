# Generated from JavaComment.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("<\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\3\2\6\2\23\n\2\r\2\16\2\24\3\3\3\3\3\3\3\3\3")
        buf.write("\3\7\3\34\n\3\f\3\16\3\37\13\3\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\6\3\6\7\6)\n\6\f\6\16\6,\13\6\3\7\7\7/\n\7\f\7\16\7")
        buf.write("\62\13\7\3\7\7\7\65\n\7\f\7\16\78\13\7\5\7:\n\7\3\7\5")
        buf.write("*\60\66\2\b\2\4\6\b\n\f\2\5\3\2\5\5\3\2\6\6\3\2\7\7\2")
        buf.write(";\2\16\3\2\2\2\4\26\3\2\2\2\6 \3\2\2\2\b$\3\2\2\2\n&\3")
        buf.write("\2\2\2\f9\3\2\2\2\16\22\5\f\7\2\17\20\5\4\3\2\20\21\5")
        buf.write("\n\6\2\21\23\3\2\2\2\22\17\3\2\2\2\23\24\3\2\2\2\24\22")
        buf.write("\3\2\2\2\24\25\3\2\2\2\25\3\3\2\2\2\26\27\5\6\4\2\27\35")
        buf.write("\5\b\5\2\30\31\5\f\7\2\31\32\5\4\3\2\32\34\3\2\2\2\33")
        buf.write("\30\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36\5\3\2\2\2\37\35\3\2\2\2 !\7\3\2\2!\"\7\t\2\2\"#\7")
        buf.write("\3\2\2#\7\3\2\2\2$%\7\13\2\2%\t\3\2\2\2&*\7\4\2\2\')\n")
        buf.write("\2\2\2(\'\3\2\2\2),\3\2\2\2*+\3\2\2\2*(\3\2\2\2+\13\3")
        buf.write("\2\2\2,*\3\2\2\2-/\n\3\2\2.-\3\2\2\2/\62\3\2\2\2\60\61")
        buf.write("\3\2\2\2\60.\3\2\2\2\61:\3\2\2\2\62\60\3\2\2\2\63\65\n")
        buf.write("\4\2\2\64\63\3\2\2\2\658\3\2\2\2\66\67\3\2\2\2\66\64\3")
        buf.write("\2\2\2\67:\3\2\2\28\66\3\2\2\29\60\3\2\2\29\66\3\2\2\2")
        buf.write(":\r\3\2\2\2\b\24\35*\60\669")
        return buf.getvalue()


class JavaCommentParser ( Parser ):

    grammarFileName = "JavaComment.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\n'", "'{'", "'\n//'", "'*/\n'", "'/**'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "END_SYMBOL", "TEXT", "WS", "NL", "IGNORED" ]

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
    T__2=3
    T__3=4
    T__4=5
    LINE_COMMENT=6
    BLOCK_COMMENT=7
    END_SYMBOL=8
    TEXT=9
    WS=10
    NL=11
    IGNORED=12

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
            return self.getTypedRuleContext(JavaCommentParser.IgnoredPreambleContext,0)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaCommentParser.CommentContext)
            else:
                return self.getTypedRuleContext(JavaCommentParser.CommentContext,i)


        def ignored(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaCommentParser.IgnoredContext)
            else:
                return self.getTypedRuleContext(JavaCommentParser.IgnoredContext,i)


        def getRuleIndex(self):
            return JavaCommentParser.RULE_sourceFile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSourceFile" ):
                listener.enterSourceFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSourceFile" ):
                listener.exitSourceFile(self)




    def sourceFile(self):

        localctx = JavaCommentParser.SourceFileContext(self, self._ctx, self.state)
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
                if not (_la==JavaCommentParser.T__0):
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

        def blockComment(self):
            return self.getTypedRuleContext(JavaCommentParser.BlockCommentContext,0)


        def codeDeclaration(self):
            return self.getTypedRuleContext(JavaCommentParser.CodeDeclarationContext,0)


        def ignoredPreamble(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaCommentParser.IgnoredPreambleContext)
            else:
                return self.getTypedRuleContext(JavaCommentParser.IgnoredPreambleContext,i)


        def comment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JavaCommentParser.CommentContext)
            else:
                return self.getTypedRuleContext(JavaCommentParser.CommentContext,i)


        def getRuleIndex(self):
            return JavaCommentParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = JavaCommentParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.blockComment()
            self.state = 21
            self.codeDeclaration()
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 22
                    self.ignoredPreamble()
                    self.state = 23
                    self.comment() 
                self.state = 29
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
            return self.getToken(JavaCommentParser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return JavaCommentParser.RULE_blockComment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockComment" ):
                listener.enterBlockComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockComment" ):
                listener.exitBlockComment(self)




    def blockComment(self):

        localctx = JavaCommentParser.BlockCommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_blockComment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(JavaCommentParser.T__0)
            self.state = 31
            self.match(JavaCommentParser.BLOCK_COMMENT)
            self.state = 32
            self.match(JavaCommentParser.T__0)
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
            return self.getToken(JavaCommentParser.TEXT, 0)

        def getRuleIndex(self):
            return JavaCommentParser.RULE_codeDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCodeDeclaration" ):
                listener.enterCodeDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCodeDeclaration" ):
                listener.exitCodeDeclaration(self)




    def codeDeclaration(self):

        localctx = JavaCommentParser.CodeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_codeDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(JavaCommentParser.TEXT)
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
            return JavaCommentParser.RULE_ignored

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnored" ):
                listener.enterIgnored(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnored" ):
                listener.exitIgnored(self)




    def ignored(self):

        localctx = JavaCommentParser.IgnoredContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ignored)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(JavaCommentParser.T__1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 37
                    _la = self._input.LA(1)
                    if _la <= 0 or _la==JavaCommentParser.T__2:
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
            return JavaCommentParser.RULE_ignoredPreamble

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnoredPreamble" ):
                listener.enterIgnoredPreamble(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnoredPreamble" ):
                listener.exitIgnoredPreamble(self)




    def ignoredPreamble(self):

        localctx = JavaCommentParser.IgnoredPreambleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ignoredPreamble)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 43
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==JavaCommentParser.T__3:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 48
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1+1:
                        self.state = 49
                        _la = self._input.LA(1)
                        if _la <= 0 or _la==JavaCommentParser.T__4:
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume() 
                    self.state = 54
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





