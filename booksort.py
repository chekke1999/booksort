#!/usr/bin/env python3
import sys,pathlib
from zipfile import ZipFile

PathObj = pathlib.Path(sys.argv[1])
COMP_LIST = ["zip","rar"]


#指定した拡張子のファイル検索
def sarchfile(Formatlist):
    for Format in Formatlist:
        for p in PathObj.glob(f"**/*.{Format}"):
            yield p

with open("./list.txt", mode="a") as tfile:
    for FullPath in sarchfile(COMP_LIST):
        tfile.write(str(FullPath) + "\n")
        with ZipFile(FullPath) as ZipF:
            for f in ZipF.namelist():
                tfile.write(f"    {f}\n")