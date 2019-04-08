grammar RustComment;

/*
 * Parser Rules
 */

sourceFile :
    ignoredPreamble (comment ignored)+ EOF
    ;

comment :
    NL blockComment codeDeclaration (e comment)*
    ;

blockComment :
    BLOCK_COMMENT NL
    ;

codeDeclaration :
    TEXT (NL TEXT)* END_SYMBOL
    ;

ignored :
    END_SYMBOL ~'\n//'*?
    ;

ignoredPreamble :
    ~'/**'*?
    ;

WS :
    [ \t]+ -> skip
    ;

LINE_COMMENT :
    '//' .*? '\r'? '\n' -> skip
    ;

BLOCK_COMMENT :
    '/**' .*? '*/'
    ;

END_SYMBOL :
    '{'
    | ';'
    ;

fragment
TEXT_FRAGMENT: [\t0-9<>\-_.~^#@=*|+;:,`'"&a-zA-Z()/\\!%[\]] ;

fragment
TEXT_AND_SPACE: TEXT_FRAGMENT | WS ;

TEXT :
    TEXT_FRAGMENT+ TEXT_AND_SPACE*
    ;

NL :
    '\r'? '\n'
    ;

IGNORED_ALPHA :
    [ a-zA-Z0-9}] -> skip
    ;

IGNORED_SYMBOLS :
    [()!?+.,#[\]<>"'_&:=|] -> skip
    ;
