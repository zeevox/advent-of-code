#!/bin/bash
if [ $1 -eq 0 ]; then
    day=$(date +%d)
else
    day=$(printf %02d "$1")
fi
cp --no-clobber base.py "Day${day}.py"
