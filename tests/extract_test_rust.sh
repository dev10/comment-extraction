#!/bin/sh

python ../antlr.py -l rust -o rst-out -ct 3b1789280bc1305aa01cd8fea1bb7372d46ae120 \
    -ru https://github.com/Fantom-Foundation/lachesis-rs \
    -sp rust/input/lachesis-rs \
    -f rust/input/lachesis-rs/lachesis-rs/src/hashgraph.rs

python ../antlr.py -l rust -o rst-out -ct 3b1789280bc1305aa01cd8fea1bb7372d46ae120 \
    -ru https://github.com/Fantom-Foundation/lachesis-rs \
    -sp rust/input/lachesis-rs \
    -d rust/input/lachesis-rs/lachesis-rs