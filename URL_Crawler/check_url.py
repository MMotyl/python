import csv
import requests
from enum import Enum 
import urle 
from urle import checkURL

plik = 'C:\\epr.txt'


with open(plik, newline='',encoding='UTF8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';') #, quotechar='' 
    data = list(reader)

max = len(data)

id = 1
correctRes = [200, 301, 302, 303]

dest_name = plik.replace('.txt','_report.csv')
print('Saving to {}'.format(dest_name))
with open(dest_name,'w', encoding='UTF-8') as savefile:
    savefile.write('lp;url;http;http_code;http_redirectsTo;http2https?;https;https_code;https_redirectsTo;'+'\n')

nvl = lambda x: x if x!=None else ''

for row in data:
    res = checkURL(row[0], tryOtherProt=True)    

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

    txt ='[{:04d}/{:04d}] {} http {} {} {} https {} {}'.format(id,max,
    res['URLRequested'],
    h_s, h_r, h_rs,
    hs_s, hs_r )
    
    print(txt)
    with open(dest_name,'a', encoding='UTF-8') as savefile:
        savefile.write(txt.replace(' ',';')+'\n')     
    id +=1 #tracking progress