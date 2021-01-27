import csv
# import requests
from enum import Enum 
import urle 
from urle import checkURL
import json

plik = 'D:\\Programowanie\\GIT_Python\\python\\URL_Crawler\\lista_full.txt' # jest na odwrót- full nie ma całości.
dest_name = plik.replace('.txt','_report.csv')
json_name = plik.replace('.txt','_report.json')
map_name = plik.replace('.txt','map.txt')

#@startuml 
#class "www.onet.pl" as o1
#o1 : http = 200
#class User
#User : http = 1

#User -> o1
#@enduml

with open(plik, newline='',encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';') #, quotechar='' 
    data = list(reader)

URLlist = []
URLlistMax =0

def AddUrl(url):
    global URLlistMax
    if url.strip() =='':
        return -1
    item = {"id" :URLlistMax, "url": url}
    URLlist.append(item)
    URLlistMax +=1 
    return URLlistMax-1

for line in data:
    AddUrl(line[0])

id = 1 
print('Saving to {}'.format(dest_name))
with open(dest_name,'w', encoding='UTF-8') as savefile:
    savefile.write('lp;url;http;http_code;http_redirectsTo;http2https?;https;https_code;https_redirectsTo;'+'\n')
with open(map_name,'w', encoding='UTF-8') as savefile:
    savefile.write('mapping'+'\n')


def findURL(url):
    if url.strip() =='':
        return -1
    id = 0
    for pos in URLlist:
        if pos['url'] == url:
            return pos['id']
        id +=1        
    return -1

def getRedir(pos, prot):
    protSta = prot+'Status' #'httpsStatus'
    if protSta in pos['result']:
        ref = pos['result'][protSta]
        return ref
    else:
        return ''    


def checkRow(pos):
    # row to json
    ref = getRedir(pos, 'http')
    if ref != '':
        id = findURL(ref['redirectedTo'])
        if id ==-1 :
            id = AddUrl(ref['redirectedTo'])
        if id !=-1 :    # dodanie mogło się nie udać
            ref['refID'] = id
                          
#    if 'httpsStatus' in pos['result']:
#        ref = pos['result']['httpsStatus']['redirectedTo']
    ref = getRedir(pos, 'https')
    if ref != '':
        id = findURL(ref['redirectedTo'])
        if id ==-1 :
            id = AddUrl(ref['redirectedTo'])              
        if id !=-1 :    # dodanie mogło się nie udać            
            #pos['result']['httpsStatus']['refID']= str(id)
            ref['refID']= id

for row in URLlist:
    res = checkURL(row['url'], tryOtherProt=True)    

    if 'httpStatus' in res:
        h_s  = res['httpStatus']['HTTPStatus']
        h_r  = res['httpStatus']['redirectedTo']
        h_rs = res['httpStatus']['redirectedToHTTPS']
    else: 
        h_s = ''
        h_r = ''
        h_rs =''

    if 'httpsStatus' in res:
        hs_s  = res['httpsStatus']['HTTPStatus']
        hs_r  = res['httpsStatus']['redirectedTo']
    else: 
        hs_s = ''
        hs_r = '-'

    txt ='[{:04d}/{:04d}] {} http {} {} {} https {} {}'.format(id, URLlistMax,
    res['URLRequested'],
    h_s, h_r, h_rs,
    hs_s, hs_r )
    
    row['result'] = res
    checkRow(row)
    print(txt)
    with open(dest_name,'a', encoding='UTF-8') as savefile:
        savefile.write(txt.replace(' ',';')+'\n')    
    id +=1 #tracking progress

def findPath(id, prot, path=''):
    elem = URLlist[id]
    if URLlist[id]['result']['URLRequested'].find('https://') != -1:
        path = 'httpsPath' # na razie zakłądam tylko upgrade http -> https

    pro_path = prot+'Path' # httpPath    
    if not (elem.get(pro_path) is None):
        txt = path + ' -> ' +URLlist[id][pro_path]
        return txt
    else:
        ref = getRedir(URLlist[id], prot)
        if ref != '':
            if 'refID' in ref:
                next_path = findPath(ref['refID'], prot, path)
                URLlist[id][pro_path] = next_path
                return URLlist[id]['result']['URLRequested'] + '->' + next_path
            else: 
                return URLlist[id]['result']['URLRequested']
        else: 
            return URLlist[id]['result']['URLRequested']

with open(json_name, 'w', encoding='utf-8') as f:
    json.dump(URLlist, f, ensure_ascii=False, indent=4)

for x in range(0,URLlistMax):
    pos = getRedir(URLlist[x],'http')
    if 'refID' in pos:
        next = findPath(pos['refID'],'http','')
        txt = "http: "+URLlist[x]['result']['URLRequested'] +' -> '+ next
        print(txt)
        with open(map_name,'a', encoding='UTF-8') as savefile:
            savefile.write(txt+'\n')

    pos = getRedir(URLlist[x],'https')
    if 'refID' in pos:
        next = findPath(pos['refID'],'http','')
        txt = "https: "+URLlist[x]['result']['URLRequested'] +' -> '+ next
        print(txt)
        with open(map_name,'a', encoding='UTF-8') as savefile:
            savefile.write(txt+'\n')
