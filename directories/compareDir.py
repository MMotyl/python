import os
import sys
# from pathlib import Path

if len(sys.argv) != 3:
    rootdir = 'g:\\test\\' #
    dir2    = 'g:\\dir2'
else:
    rootdir = sys.argv[1]
    dir2    = sys.argv[2]

list1 = []
list2 = []

def scan(lista, dir):
    for folder, subs, files in os.walk(dir):
        print('Analizing {}'.format(folder))
        for file in files:
            pos = {"file": file, "dir" : folder}
            lista.append(pos)

scan(list1, rootdir )            
scan(list2, dir2 )            

for pos1 in list1:
    found = False
    for x  in range(len(list2)):
        if list2[x]["file"] == pos1["file"]:
            list2.pop(x)
            found = True
            break
    pos1['found'] = found
    if not found:
        print('not found {}\{}'.format(pos1["dir"], pos1['file']))

