# Generated from GolangComment.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("C\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\7\7+\n\7\f\7\16\7.\13\7\3\7\3\7\3\7\3\b\6\b\64\n\b\r")
        buf.write("\b\16\b\65\3\b\5\b9\n\b\3\t\5\t<\n\t\3\t\3\t\5\t@\n\t")
        buf.write("\3\n\3\n\3,\2\13\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\3\2\4\b\2\13\13\"%\'@C|~~\u0080\u0080\b\2\"\"*+--")
        buf.write("C\\c|\177\177\2G\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\3\25\3\2\2\2\5\32\3\2\2\2\7\34\3")
        buf.write("\2\2\2\t\36\3\2\2\2\13\"\3\2\2\2\r&\3\2\2\2\178\3\2\2")
        buf.write("\2\21?\3\2\2\2\23A\3\2\2\2\25\26\7\f\2\2\26\27\7\61\2")
        buf.write("\2\27\30\7\61\2\2\30\31\7\"\2\2\31\4\3\2\2\2\32\33\7\f")
        buf.write("\2\2\33\6\3\2\2\2\34\35\7}\2\2\35\b\3\2\2\2\36\37\7\f")
        buf.write("\2\2\37 \7\61\2\2 !\7\61\2\2!\n\3\2\2\2\"#\7,\2\2#$\7")
        buf.write("\61\2\2$%\7\f\2\2%\f\3\2\2\2&\'\7\61\2\2\'(\7,\2\2(,\3")
        buf.write("\2\2\2)+\13\2\2\2*)\3\2\2\2+.\3\2\2\2,-\3\2\2\2,*\3\2")
        buf.write("\2\2-/\3\2\2\2.,\3\2\2\2/\60\7,\2\2\60\61\7\61\2\2\61")
        buf.write("\16\3\2\2\2\62\64\t\2\2\2\63\62\3\2\2\2\64\65\3\2\2\2")
        buf.write("\65\63\3\2\2\2\65\66\3\2\2\2\669\3\2\2\2\679\7}\2\28\63")
        buf.write("\3\2\2\28\67\3\2\2\29\20\3\2\2\2:<\7\17\2\2;:\3\2\2\2")
        buf.write(";<\3\2\2\2<=\3\2\2\2=@\7\f\2\2>@\7\17\2\2?;\3\2\2\2?>")
        buf.write("\3\2\2\2@\22\3\2\2\2AB\t\3\2\2B\24\3\2\2\2\b\2,\658;?")
        buf.write("\2")
        return buf.getvalue()


class GolangCommentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    BLOCK_COMMENT = 6
    TEXT = 7
    NL = 8
    IGNORED = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n// '", "'\n'", "'{'", "'\n//'", "'*/\n'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "TEXT", "NL", "IGNORED" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "BLOCK_COMMENT", 
                  "TEXT", "NL", "IGNORED" ]

    grammarFileName = "GolangComment.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


