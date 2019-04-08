grammar JavaComment;

/*
 * Parser Rules
 */

sourceFile
    : ignoredPreamble (comment ignored)+
    ;

comment
    : blockComment codeDeclaration (ignoredPreamble comment)*
    ;

blockComment
    : '\n' BLOCK_COMMENT '\n'
    ;

codeDeclaration
    : TEXT
    ;

ignored
    : '{' ~'\n//'*?
    ;

ignoredPreamble
    : ~'*/\n'*?
    | ~'/**'*?
    ;


LINE_COMMENT :
    '//' .*? '\r'? '\n' -> skip
    ;

BLOCK_COMMENT :
    WS? '/**' .*? '*/'
    ;

END_SYMBOL :
    '{'
    | ';'
    ;

TEXT :
    [ \t0-9<>\-_.~^#@=*|+:,`'"&a-zA-Z()/\\!%[\]]+ ('\n' TEXT END_SYMBOL)?
    ;

WS :
    [ \t]+ -> skip
    ;

NL :
    '\r'? '\n'
    ;

IGNORED
    : [ a-zA-Z()+}]
    ;