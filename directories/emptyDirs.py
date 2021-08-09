import os
import sys
from pathlib import Path

if len(sys.argv) != 3:
    rootdir = 'g:\\test\\' #
else:
    rootdir = sys.argv[1]

for folder, subs, files in os.walk(rootdir):
    lx = len(files)
    su = len(subs)
    # print("{} : has {} subdirs and has {} files".format(folder,su,lx))
    if lx+su ==0:
        print("removing {}".format(folder) )
        shutil.rmtree(folder, ignore_errors=True)
