#!/bin/sh

python ../antlr.py -l java -o rst-out -ct 3b1789280bc1305aa01cd8fea1bb7372d46ae120 \
    -ru https://github.com/Fantom-Foundation/jlachesis \
    -sp java/input/jlachesis \
    -f java/input/jlachesis/src/test/java/poset/PosetTest.java

python ../antlr.py -l java -o rst-out -ct 3b1789280bc1305aa01cd8fea1bb7372d46ae120 \
    -ru https://github.com/Fantom-Foundation/jlachesis \
    -sp java/input/jlachesis \
    -d java/input/jlachesis