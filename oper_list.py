import yaml
import os
import sys
from pathlib import Path

rootdir ='D:\\Programowanie\\HAL\\HAL-core\\public\\swagger'

def parseSwagger(path):
    print('Parsing '+path)
    try:
        with open(path, encoding="utf8") as f:   
            docs = yaml.load_all(f, Loader=yaml.FullLoader)
            for doc in docs:    # jest tylko jeden 
                if 'paths' not in doc:
                    print('invalid file! ')
                    continue
                objects = doc['paths']
                for k, v in objects.items():
                    # k = operation name
                    for oper in v.keys():
                        print('  {} {}'.format(oper, k) )
    except:
        print('error with file')

for folder, subs, files in os.walk(rootdir):
    for filename in files:
        p = Path(filename)
        if p.suffix=='.yaml':
            fn = folder+'\\'+filename          
            parseSwagger(fn)
