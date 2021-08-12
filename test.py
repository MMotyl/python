import os
import sys
from pathlib import Path

rootdir = 'E:\\Dyski\\OneDrive - T-Mobile Polska S.A\\BR-5009 Taurus\\SWAGERY\\'

for folder, subs, files in os.walk(rootdir):
    for filename in files:
        p = Path(filename)
        if p.suffix=='.yaml':
            fn = folder+filename
            print (fn)
