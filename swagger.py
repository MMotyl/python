# pip install pyyaml
import yaml

## zamiana swaggera na plant z relacjami encji

# path = 'D:\\Programowanie\\HAL\\HAL-core\\public\\swagger\\payment-management.yaml'
path = 'D:\\Programowanie\\Uniqa\\API\\contractor.yaml'
outPath = 'D:\\Programowanie\\Uniqa\\API\\'

out = []    #output
relations = [] # for refferences.
showFields = False

with open(path) as f:   
    docs = yaml.load_all(f, Loader=yaml.FullLoader)

    for doc in docs:    # jest tylko jeden 
        objects = doc['definitions']
        for k, v in objects.items():
            txt = 'object '+ k+ ' {' # append wymaga pojedynczego obiektu
            out.append(txt) 
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

# saving result
base = path.split('\\')[-1]
filename = outPath + base.replace('yaml','puml')
print ('saving to ',filename)

f = open(filename, "w")
f.writelines('@startUML\n')
f.writelines('\' Butter\n')
f.writelines('\' based on :'+path.split('\\')[-1]+'\n')
f.writelines('TITLE Objects relation in '+base+'\n')
for line in out:
    f.writelines(line+'\n')

for line in relations:
    f.writelines(line+'\n')

f.writelines('@endUML\n')
f.close()    

print ('file saved')