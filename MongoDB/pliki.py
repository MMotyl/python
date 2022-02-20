import glob, os
from pathlib import Path
import sys

## biblioteka pomocnicza - iteracja po plikach!

def filesInDir(path):
    for folder, subs, files in os.walk(path):
        for filename in files:
#            fn = folder+'\\'+filename          
            yield folder, filename          
        