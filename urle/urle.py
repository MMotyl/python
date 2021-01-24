import http.client
from enum import Enum
import base64

Protocol = Enum('Protocol', 'http https none')
Operation = Enum('Operation', 'GET HEAD')

request_payload = ''
request_headers = {}

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

def CallURL(data, operation = Operation.HEAD, ):
    if data['protocol'] == Protocol.http.name:
        conn = http.client.HTTPConnection(data['host'])
    else:
        conn = http.client.HTTPSConnection(data['host'])

    try:    
        conn.request(operation.name , data['path'], request_payload, request_headers)
        res = conn.getresponse()        
        data["HTTPStatus"] = res.status
        data['redirectedTo'] = res.headers['Location']
    except:    
        data["URLStatus"] = 'ERR'

    return data

def CheckHTTPSRedirect(url, redirect):
    return url.replace('http://', 'https://') == redirect
    
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
    

    status = {"protocol": try_protocol.name,
            "HTTPStatus":"", 
            "redirectedTo":"",  "redirectedToHTTPS" :""}

    data = {"URLRequested": url, "host": host, "path": path, "statuses": [status]}

    data = CallURL(data, operation)
    if CheckHTTPSRedirect(url,data["redirectedTo"]):
        data["redirectedToHTTPS"] = 'yes'
    else:
        data["redirectedToHTTPS"] = 'no'

    data2 = data.copy()
    if tryOtherProt:
        if try_protocol == Protocol.http:
            data2['protocol'] =Protocol.https.name
        else:    
            data2['protocol'] =Protocol.http.name
        data2 = CallURL(data2, operation)    
        if CheckHTTPSRedirect(url,data2["redirectedTo"]):
            data2["redirectedToHTTPS"] = 'yes'
        else:
            data2["redirectedToHTTPS"] = 'no'        
    else:
        data2['protocol'] =Protocol.none.name
        data2['HTTPStatus'] = 'not tried'

    return data, data2

d1, d2 = checkURL('https://www.axadirect.pl/kalkulator/assistance-w-podrozy/insurance',operation=Operation.GET, tryOtherProt=False, user='butter', password='123')    
# http://assistancewpodrozy.pl
