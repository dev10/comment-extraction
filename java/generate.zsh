#!/bin/zsh

fpath=( ~/.zfunc "${fpath[@]}" )
autoload -Uz antlr4
autoload -Uz grun

antlr4 -Dlanguage=Python3 JavaComment.g4
