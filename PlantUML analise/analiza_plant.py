import glob, os
from pathlib import Path
import sys
import string
import re

fileName = 'e:\Dyski\OneDrive - T-Mobile Polska S.A\BR-5009 Taurus\SWAGERY\Projects\BR-5009Taurus\I_PAY\IPAY-19 Fiskalizacja.plantuml'
initPath = 'e:\\Dyski\\OneDrive - T-Mobile Polska S.A\\BR-5009 Taurus\\SWAGERY\\Projects\\BR-5009Taurus\\'
initPath = 'C:\\GIT\\SD\\SolutionDesign\\Projects\\BR-5009Taurus\\' #I_Join_Login\\

operacje = []
lines = []
participants = []

def readFile(fileName):
    global lines
    lines.clear()

    global participants
    participants.clear()

    print('Analiza {}'.format(fileName))
    with open(fileName, encoding='UTF-8') as plik:
        lines = plik.readlines()

def checkLine(line):
    #odrzucenie śmieciowych linii
    badStarts = ['\'', '|<#', '//', '==</', '>x', '/']
    ok = True
    for elem in badStarts:
        ok = ok and not line.lstrip().startswith(elem) # komentarze!
        if not ok:
            break
    return ok

def NormalizeLine(line):
    replacements = { '++' : '',  
        ':'    : ' : ',
        '-->>' : '->',
        '->>'  : '->',        
        '-->'  : '->',
        '->]'  : '->',
        '->'   : ' -> ' }
        
    regExp = re.findall(r'\[[-#0-9a-z, ]*\]', line, re.I) # re.I = A-Z
    for pos in regExp:  #'[-[#green]>API: [RQS-217] OPERATION /resource' --> [->API:  OPERATION /resource
        line = line.replace(pos,'')

    for fr, to in replacements.items():
        line = line.replace(fr,to)    

    return line

def RemapAlias(line):
    global participants
    res = line
    for elem in participants:
        if line == elem['alias']:
            res = elem['nazwa']
            break
    return res

def parseLine(line):
    src = line
    line = NormalizeLine(line)
    ok = checkLine(line)
    res = {'client': None, 'server':'', 'method': ''}
    elems = line.split()

    if elems[0].startswith('-'): # lub 1 - inaczej nie powinno być!
        ofset = -1
    elif elems[0].startswith('['): #[-[#green]>
        ofset = 0 # było -3 dla '[ -'
    else:    
        ofset = 0
        res['client'] = RemapAlias( elems[0] )
    res['server'] = RemapAlias( elems[2+ofset] )
    oper = ' '.join(elems[4+ofset:])
    res['method'] = oper
    ok = ok and (res['client']!= res['server']) # usunięcie wywołań samego siebie
    return ok, res

def sortName(val): # do sortowania
    return val['server']

def addParticipant(line):
    global participants
    if not checkLine(line):
        return
    line = line.replace('participant','') #stała, usuwamy
    spl = line.split('as')  #as dzieli na nazawa as alias + śmieci
    name  = spl[0].replace('"','')  #tu mamy nazwę. jeśli dłuższa, to ma "
    if len(spl)==1:
        return
    spl2  = spl[1].split()  # a tu inteesuje nas tylko pierszy element
    alias = spl2[0]
    partic ={ "nazwa": name, "alias": alias}
    participants.append(partic)
    #print(partic)

def parseFile():
    global operacje
    global participants
    for line in lines:
        par = line.lower().find('participant ')
        if par >=0:
            addParticipant(line)
        pos = line.find(">")
        if pos>0:
            ok, elem = parseLine(line)
            if ok:
                operacje.append(elem)
                print(elem)

#fxx = r'e:\Dyski\OneDrive - T-Mobile Polska S.A\BR-5009 Taurus\SWAGERY\Projects\BR-5009Taurus\I_Join_Checkout\UC-164 Synchronizacja zasobów.plantuml'
#fxx = fxx.replace('\\','\\\\')
#readFile(fxx)
#parseFile()    


for folder, subs, files in os.walk(initPath):
    for filename in files:
        p = Path(filename)
        if p.suffix=='.plantuml':
            fn = folder+'\\'+filename          
            readFile(fn)
            parseFile()    

print('===<WYNIK>===')
operacje.sort(key=sortName)

servers =[] # unikalna lista serverów
for x in operacje:
    servers.append(x['server'])

servers = ( list (set (servers) ) )
for serv in servers:
    oper = [l['method'] for i,l in enumerate(operacje) if serv in l['server']]
    oper = list( set (oper) ) # unikalność
    print('-------------------------------')
    print('Operacje dla {}'.format(serv) )
    for op in oper:
        print('     {}'.format(op) )


#for el in operacje:
#    print(el)