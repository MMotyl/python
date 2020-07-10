import os
import sys
import shutil
from pathlib import Path

rootdir = 'e:\\eBooki\\' #sys.argv[1]
#rootdir = 'z:\\' #sys.argv[1]
os.system('chcp 1250')

for folder, subs, files in os.walk(rootdir):
    lx = len(files)
    su = len(subs)
    # print("{} : has {} subdirs and has {} files".format(folder,su,lx))
    if lx+su ==0:
        print("removing {}".format(folder) )
        shutil.rmtree(folder, ignore_errors=True)
