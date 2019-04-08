grammar GolangComment;

/*
 * Parser Rules
 */

sourceFile
    : ignoredPreamble (comment ignored)+
    ;

comment
    : lineComment codeDeclaration
    | blockComment codeDeclaration
    ;

lineComment
    : '\n// ' ~'\n'*? '\n'
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
    : ~'\n//'*?
    | ~'*/\n'*?
    ;

BLOCK_COMMENT
    : '/*' .*? '*/'
    ;

TEXT
    : [ \t0-9<>\-_.~^#=*|+:;,`'"&a-zA-Z()/\\!%[\]]+
    | '{'
    ;

NL
    : '\r'? '\n' | '\r';

IGNORED
    : [ a-zA-Z()+}]
    ;