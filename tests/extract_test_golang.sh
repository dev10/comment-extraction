#!/bin/sh

python ../antlr.py -l golang -o rst-out -ct 842c9ef9fe8ba2c2737b721647d4950dcacf4c1b \
    -ru https://github.com/Fantom-Foundation/go-lachesis \
    -sp golang/input/go-lachesis \
    -f golang/input/go-lachesis/src/poset/poset_test.go

python ../antlr.py -l golang -o rst-out -ct 842c9ef9fe8ba2c2737b721647d4950dcacf4c1b \
    -ru https://github.com/Fantom-Foundation/go-lachesis \
    -sp golang/input/go-lachesis \
    -d golang/input/go-lachesis
