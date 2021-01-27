import http.client
from enum import Enum
import base64
import json

Protocol = Enum('Protocol', 'http https none')
Operation = Enum('Operation', 'GET HEAD')

request_payload = ''
request_headers = {}
req_timeout = 1

def cleanURL(url):
    prot = Protocol.none #assumed protocol
    if url.find('https://') != -1:
        prot = Protocol.https
    if url.find('http://') != -1:
        prot = Protocol.http

    badCharacters = [' ', chr(13), chr(10), 'http://', 'https://']
    for pos in badCharacters:
        url = url.replace(pos,'')

    return url, prot

def splitURL(url):
    chunk = url.split('/')
    host = chunk[0]
    path ='/' + '/'.join(chunk[1:])

    return host, path

def CallURL(data, operation = Operation.HEAD, prot = Protocol.https):
    if prot.name == Protocol.http.name:
        conn = http.client.HTTPConnection(data['host'],timeout=req_timeout)
    else:
        conn = http.client.HTTPSConnection(data['host'],timeout=req_timeout)

    try:    
        conn.request(operation.name , data['path'], request_payload, request_headers)
        res = conn.getresponse()        
        redirect = ''
        if res.headers['Location'] != None:
            redirect = res.headers['Location']


        status  = {
            "protocol": prot.name,  
            "HTTPStatus": res.status, 
            "redirectedTo": redirect,
            "redirectedToHTTPS" :""}
        if prot.name == Protocol.http.name:
            status["redirectedToHTTPS"] = CheckHTTPSRedirect(data["URLRequested"],status["redirectedTo"])
        else:     
            status["redirectedToHTTPS"] ='-' #does not apply
    except:    
        status  = {
            "protocol": prot.name,  
            "HTTPStatus": 'ERR!', 
            "redirectedTo":"",
            "redirectedToHTTPS" :""}

    data[prot.name+'Status'] = status
    data["statuses"].append(status)

    return data

def CheckHTTPSRedirect(url, redirect):
    if url.find('http') ==-1 : # request może być bez prot.
        url = 'http://'+url
    if redirect[-1] =='/':
        url = url+'/'
    res = url.replace('http://', 'https://') == redirect
    if res:
        return "Y"
    else:
        return "N"    
    
def checkURL(url, protocol = Protocol.https, operation = Operation.HEAD, tryOtherProt = False, user ='', password =''):
    global request_headers
    cleanedUrl, assumed_protocol = cleanURL(url)
    host, path = splitURL(cleanedUrl)

    if assumed_protocol == Protocol.none:
        try_protocol = protocol
    else: 
        try_protocol = assumed_protocol

    if len(user)>0:
        auth = user+':'+password
        base64_auth = base64.b64encode(auth.encode("UTF-8"))
        request_headers = { 'Authorization': "Basic "+str(base64_auth) }  
    

    data = {"URLRequested": url, "host": host, "path": path, "statuses": []}
    data = CallURL(data, operation, try_protocol)

    if tryOtherProt and assumed_protocol == Protocol.none:
        if try_protocol == Protocol.http:
           try_protocol = Protocol.https
        else:    
           try_protocol = Protocol.http

        data = CallURL(data, operation, try_protocol)    
    return data #json.dumps(data, indent=4, sort_keys=True)

#data = checkURL('assistancewpodrozy.pl',operation=Operation.GET, tryOtherProt=True)    
#print(data)

# http://assistancewpodrozy.pl
# 'https://www.axadirect.pl/kalkulator/assistance-w-podrozy/insurance'
