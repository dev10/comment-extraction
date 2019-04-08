# Generated from JavaComment.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\7\7\60\n\7\f\7\16\7\63\13\7\3\7")
        buf.write("\5\7\66\n\7\3\7\3\7\3\7\3\7\3\b\5\b=\n\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\7\bD\n\b\f\b\16\bG\13\b\3\b\3\b\3\b\3\t\3\t\3\n")
        buf.write("\6\nO\n\n\r\n\16\nP\3\n\3\n\3\n\3\n\5\nW\n\n\3\13\6\13")
        buf.write("Z\n\13\r\13\16\13[\3\13\3\13\3\f\5\fa\n\f\3\f\3\f\3\r")
        buf.write("\3\r\4\61E\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\3\2\6\4\2==}}\t\2\13\13\"%\'<>@B|")
        buf.write("~~\u0080\u0080\4\2\13\13\"\"\b\2\"\"*+--C\\c|\177\177")
        buf.write("\2m\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3")
        buf.write("\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t#\3\2\2\2\13\'\3\2\2")
        buf.write("\2\r+\3\2\2\2\17<\3\2\2\2\21K\3\2\2\2\23N\3\2\2\2\25Y")
        buf.write("\3\2\2\2\27`\3\2\2\2\31d\3\2\2\2\33\34\7\f\2\2\34\4\3")
        buf.write("\2\2\2\35\36\7}\2\2\36\6\3\2\2\2\37 \7\f\2\2 !\7\61\2")
        buf.write("\2!\"\7\61\2\2\"\b\3\2\2\2#$\7,\2\2$%\7\61\2\2%&\7\f\2")
        buf.write("\2&\n\3\2\2\2\'(\7\61\2\2()\7,\2\2)*\7,\2\2*\f\3\2\2\2")
        buf.write("+,\7\61\2\2,-\7\61\2\2-\61\3\2\2\2.\60\13\2\2\2/.\3\2")
        buf.write("\2\2\60\63\3\2\2\2\61\62\3\2\2\2\61/\3\2\2\2\62\65\3\2")
        buf.write("\2\2\63\61\3\2\2\2\64\66\7\17\2\2\65\64\3\2\2\2\65\66")
        buf.write("\3\2\2\2\66\67\3\2\2\2\678\7\f\2\289\3\2\2\29:\b\7\2\2")
        buf.write(":\16\3\2\2\2;=\5\25\13\2<;\3\2\2\2<=\3\2\2\2=>\3\2\2\2")
        buf.write(">?\7\61\2\2?@\7,\2\2@A\7,\2\2AE\3\2\2\2BD\13\2\2\2CB\3")
        buf.write("\2\2\2DG\3\2\2\2EF\3\2\2\2EC\3\2\2\2FH\3\2\2\2GE\3\2\2")
        buf.write("\2HI\7,\2\2IJ\7\61\2\2J\20\3\2\2\2KL\t\2\2\2L\22\3\2\2")
        buf.write("\2MO\t\3\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2Q")
        buf.write("V\3\2\2\2RS\7\f\2\2ST\5\23\n\2TU\5\21\t\2UW\3\2\2\2VR")
        buf.write("\3\2\2\2VW\3\2\2\2W\24\3\2\2\2XZ\t\4\2\2YX\3\2\2\2Z[\3")
        buf.write("\2\2\2[Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\b\13\2\2^\26")
        buf.write("\3\2\2\2_a\7\17\2\2`_\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\7")
        buf.write("\f\2\2c\30\3\2\2\2de\t\5\2\2e\32\3\2\2\2\13\2\61\65<E")
        buf.write("PV[`\3\b\2\2")
        return buf.getvalue()


class JavaCommentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    LINE_COMMENT = 6
    BLOCK_COMMENT = 7
    END_SYMBOL = 8
    TEXT = 9
    WS = 10
    NL = 11
    IGNORED = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'", "'{'", "'\n//'", "'*/\n'", "'/**'" ]

    symbolicNames = [ "<INVALID>",
            "LINE_COMMENT", "BLOCK_COMMENT", "END_SYMBOL", "TEXT", "WS", 
            "NL", "IGNORED" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "LINE_COMMENT", 
                  "BLOCK_COMMENT", "END_SYMBOL", "TEXT", "WS", "NL", "IGNORED" ]

    grammarFileName = "JavaComment.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        self.nesting = 0


