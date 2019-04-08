#!/bin/zsh

fpath=( ~/.zfunc "${fpath[@]}" )
autoload -Uz antlr4
autoload -Uz grun

antlr4 -Dlanguage=Python3 GolangComment.g4
#antlr4 -Dlanguage=Java GolangComment.g4
#grun Golang.g4 golang -tokens