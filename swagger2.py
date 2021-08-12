# pip install pyyaml
import yaml
import os
import sys
from pathlib import Path

## zamiana swaggera na plant z relacjami encji

outPathX = 'C:\\OneDrive\\OneDrive - UNIQA Group 365\\Swaggery\\OUT\\'
# rootdir = 'D:\\Programowanie\\HAL\\HAL-core\\public\\swagger\\' 
rootdir = 'C:\\GIT\\interfaces-agreements\\Domains\\'
# rootdir = 'e:\Dyski\OneDrive - T-Mobile Polska S.A\BR-5009 Taurus\SWAGERY\Swaggers\

out = []    #output
relations = [] # for refferences.
showFields = True # False

def parseSwagger(path):
    out.clear()
    relations.clear()
    print('Parsing '+path)
    with open(path, encoding="utf8") as f:   
        docs = yaml.load_all(f, Loader=yaml.FullLoader)
        try:
            for doc in docs:    # jest tylko jeden 
                if 'definitions' not in doc:
                    print('invalid file! ')
                    break
                objects = doc['definitions']
                for k, v in objects.items():
                    txt = 'object '+ k+ ' {' # append wymaga pojedynczego obiektu
                    out.append(txt) 
                    if 'properties' not in v:
                        out.append('}\n')                             
                        print('invalid definition! ')
                        continue
                    pola = v['properties'] #pola w typie
                    for pole in pola:       
                        if '$ref' in pola[pole]:
                            rel = k + ' -- '+ pola[pole]['$ref'].split('/')[-1] + ' : '+ pole
                            relations.append(rel)
                        if 'type' in pola[pole] and pola[pole]['type']=='array':
                            tab = pola[pole]['items']
                            if '$ref' in tab:
                                rel = k + ' -- '+ tab['$ref'].split('/')[-1] + ' : '+ pole+ ' []'
                                relations.append(rel)
                        if showFields:
                            txt = '  '+pole
                            out.append(txt)
                    out.append('}\n')     
        except:
            print('parsing error')               


def save(outPath, path):
    # saving result
    base = path.split('\\')[-1]
    filename = outPath + base.replace('yaml','puml')
    print ('saving to ',filename,end ='')

    f = open(filename, "w")
    f.writelines('@startUML\n')
    f.writelines('\' Butter v 1.1 \n')
    f.writelines('\' based on :'+path.split('\\')[-1]+'\n')
    f.writelines('TITLE Objects relation in '+base+'\n')
    for line in out:
        f.writelines(line+'\n')

    for line in relations:
        f.writelines(line+'\n')

    f.writelines('@endUML\n')
    f.close()    

    print ('. File saved')


for folder, subs, files in os.walk(rootdir):
    for filename in files:
        p = Path(filename)
        if p.suffix=='.yaml':
            fn = folder+'\\'+filename          
            parseSwagger(fn)
            save(outPathX, fn)

#fn = 'D:\\Programowanie\\HAL\\HAL-core\\public\\swagger\\activation-configuration.yaml' 
#parseSwagger(fn)
#save(outPathX, fn)

