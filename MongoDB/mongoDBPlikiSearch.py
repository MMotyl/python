from pymongo import MongoClient
import pymongo
import re

connectionStr = 'mongodb://admin:%5BBtr0Btr%5D@192.168.0.101:27017/?authSource=admin&readPreference=primary&ssl=false'

client = MongoClient(connectionStr)
db = client['dev']  
mycol = db["files"] 

myquery = { "name": "LEM" } 
myquery = { "name": { "$regex": "^.*docker.*" , '$options' : 'i'} } # wersja prosta case insensitive!


fields  = {"_id":0, "name":1, "path":1 } # które kolumny ma zwracać

for x in mycol.find(myquery , fields):
  print(x)
  
# find().sort("name")  
# sort("name", 1) #ascending
# sort("name", -1) #descending