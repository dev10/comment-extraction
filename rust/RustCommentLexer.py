# Generated from RustComment.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("g\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\4\6\4%\n\4\r\4\16\4&\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\7\5/\n\5\f\5\16\5\62\13\5\3\5\5")
        buf.write("\5\65\n\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\7\6@\n\6")
        buf.write("\f\6\16\6C\13\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\5")
        buf.write("\tN\n\t\3\n\6\nQ\n\n\r\n\16\nR\3\n\7\nV\n\n\f\n\16\nY")
        buf.write("\13\n\3\13\5\13\\\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\4\60A\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17\2\21")
        buf.write("\2\23\t\25\n\27\13\31\f\3\2\7\4\2\13\13\"\"\4\2==}}\b")
        buf.write("\2\13\13#%\'@B|~~\u0080\u0080\7\2\"\"\62;C\\c|\177\177")
        buf.write("\f\2#%(+-.\60\60<<>A]]__aa~~\2l\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33")
        buf.write("\3\2\2\2\5\37\3\2\2\2\7$\3\2\2\2\t*\3\2\2\2\13:\3\2\2")
        buf.write("\2\rG\3\2\2\2\17I\3\2\2\2\21M\3\2\2\2\23P\3\2\2\2\25[")
        buf.write("\3\2\2\2\27_\3\2\2\2\31c\3\2\2\2\33\34\7\f\2\2\34\35\7")
        buf.write("\61\2\2\35\36\7\61\2\2\36\4\3\2\2\2\37 \7\61\2\2 !\7,")
        buf.write("\2\2!\"\7,\2\2\"\6\3\2\2\2#%\t\2\2\2$#\3\2\2\2%&\3\2\2")
        buf.write("\2&$\3\2\2\2&\'\3\2\2\2\'(\3\2\2\2()\b\4\2\2)\b\3\2\2")
        buf.write("\2*+\7\61\2\2+,\7\61\2\2,\60\3\2\2\2-/\13\2\2\2.-\3\2")
        buf.write("\2\2/\62\3\2\2\2\60\61\3\2\2\2\60.\3\2\2\2\61\64\3\2\2")
        buf.write("\2\62\60\3\2\2\2\63\65\7\17\2\2\64\63\3\2\2\2\64\65\3")
        buf.write("\2\2\2\65\66\3\2\2\2\66\67\7\f\2\2\678\3\2\2\289\b\5\2")
        buf.write("\29\n\3\2\2\2:;\7\61\2\2;<\7,\2\2<=\7,\2\2=A\3\2\2\2>")
        buf.write("@\13\2\2\2?>\3\2\2\2@C\3\2\2\2AB\3\2\2\2A?\3\2\2\2BD\3")
        buf.write("\2\2\2CA\3\2\2\2DE\7,\2\2EF\7\61\2\2F\f\3\2\2\2GH\t\3")
        buf.write("\2\2H\16\3\2\2\2IJ\t\4\2\2J\20\3\2\2\2KN\5\17\b\2LN\5")
        buf.write("\7\4\2MK\3\2\2\2ML\3\2\2\2N\22\3\2\2\2OQ\5\17\b\2PO\3")
        buf.write("\2\2\2QR\3\2\2\2RP\3\2\2\2RS\3\2\2\2SW\3\2\2\2TV\5\21")
        buf.write("\t\2UT\3\2\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2X\24\3\2\2")
        buf.write("\2YW\3\2\2\2Z\\\7\17\2\2[Z\3\2\2\2[\\\3\2\2\2\\]\3\2\2")
        buf.write("\2]^\7\f\2\2^\26\3\2\2\2_`\t\5\2\2`a\3\2\2\2ab\b\f\2\2")
        buf.write("b\30\3\2\2\2cd\t\6\2\2de\3\2\2\2ef\b\r\2\2f\32\3\2\2\2")
        buf.write("\13\2&\60\64AMRW[\3\b\2\2")
        return buf.getvalue()


class RustCommentLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    LINE_COMMENT = 4
    BLOCK_COMMENT = 5
    END_SYMBOL = 6
    TEXT = 7
    NL = 8
    IGNORED_ALPHA = 9
    IGNORED_SYMBOLS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n//'", "'/**'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "LINE_COMMENT", "BLOCK_COMMENT", "END_SYMBOL", "TEXT", 
            "NL", "IGNORED_ALPHA", "IGNORED_SYMBOLS" ]

    ruleNames = [ "T__0", "T__1", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "END_SYMBOL", "TEXT_FRAGMENT", "TEXT_AND_SPACE", "TEXT", 
                  "NL", "IGNORED_ALPHA", "IGNORED_SYMBOLS" ]

    grammarFileName = "RustComment.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


