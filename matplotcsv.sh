#! /usr/bin/env bash

directory=$0
directory=${directory%/matplotcsv.sh}
python3 $directory/plot.py $@