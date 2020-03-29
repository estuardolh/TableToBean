#!/bin/bash
cp $1 ./src/
cd ./src/ && python TableToBean.py $1
mv -f ./output/ ../output/
#mv -f ./src/output/ ../output
