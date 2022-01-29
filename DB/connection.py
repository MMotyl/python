from distutils.util import execute
from multiprocessing import connection
from sqlite3 import Cursor
import pyodbc
import json

fields =[]

def connect():
    server = '.\SQL1.database.windows.net'
    server = '192.168.0.100'
    database = 'dev'
    username = 'python'
    password = 'Python2022' 
    driver= '{ODBC Driver 17 for SQL Server}'    
    conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return(conn)

def finalize(conn):
    conn.close()
    
def getSelect(conn, SQLquery):
    cursor=conn.cursor()
    cursor.execute(SQLquery)
    
    # słownik pól
    global fields
    fields = []
    for pos in cursor.description:
        fields.append(pos[0])
        
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        yield row

    cursor.close()

def Row2Json(row, pretty =False):
    event  = {
            "id": row[0],  
            "ver": row[ fields.index('parent_id') ],
            "details": [] 
            }    
    event['value'] = row[3] # alternatywne podejście 
    event["details"].append( {'arg1' : str(row[4]) } )
    event["details"].append( {'arg2' : str(row[4]) } ) # wiem, to samo pole    

    sub = {
            "arg3" : str(row[4]),
            "arg4_3" : "stała"            
          }
    event["OtherDetails"] = sub 
    
    if pretty:
        txt = json.dumps(event, ensure_ascii=False, indent=4)    
    else: 
        txt = event    
    return (txt)

connection = connect()
sql = 'select id, parent_id, c4, c5, c6 from testPerf' #testPerf

for row in getSelect(connection, sql):
    print ( Row2Json(row) )
    
finalize(connection)