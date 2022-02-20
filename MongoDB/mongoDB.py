from pymongo import MongoClient
import pymongo
from pliki import filesInDir

connectionStr = 'mongodb://admin:%5BBtr0Btr%5D@192.168.0.101:27017/?authSource=admin&readPreference=primary&ssl=false'

client = MongoClient(connectionStr)
db = client['dev'] # utworzenie / pobranie 
    
# for name in client.list_database_names():
#    print (name)

# collist = db.list_collection_names()
# if "customers" in collist:
 # print("The collection exists.")

mycol = db["files"] # tworzenie kolekcji


# mydict = { "name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]
# x = mycol.insert_many(mylist)

for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)