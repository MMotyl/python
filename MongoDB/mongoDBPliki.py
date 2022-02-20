from pymongo import MongoClient
import pymongo
from pliki import filesInDir

connectionStr = 'mongodb://admin:%5BBtr0Btr%5D@192.168.0.101:27017/?authSource=admin&readPreference=primary&ssl=false'

## insert do bazy mongo

client = MongoClient(connectionStr)
db = client['dev'] # utworzenie / pobranie 
    
mycol = db["files"] # tworzenie kolekcji

initPath = 'e:\\eBooki'
id = 0

for folder, file in filesInDir(initPath):
    fileRec  = {
            "id": id,
            "name": file,
            "path": folder,
            "author": "",
            "series": []
            }     
    x = mycol.insert_one(fileRec)     
    id = id+1
    print('#',end='')
    if id%100 ==0:
        print(id)