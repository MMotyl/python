# https://pl.spoj.com/problems/BFNTEST/
import fileinput
groupComment = False

def checkLine(line):
    global groupComment
    tmpComment = False
    line = line.replace('\n','')
    kon  = line.find('*/')
    pocz = line.find('/*')

    if (kon!= -1 ) and (pocz!= -1):
        tmpComment = True
        txt = line[0:pocz]+line[kon+2:len(line)]
        if txt == '': txt =' '
        print(txt.rstrip())
    if not groupComment and not tmpComment and (pocz!= -1):
        groupComment = True
        print(line.split('/*')[0])
    if groupComment & (kon!= -1):
        groupComment = False
        tmpComment = True        
    if not (groupComment or tmpComment):
        print(line.split('//')[0])

#for poz in fileinput.input():
#    checkLine(line)

path = 'D:\\Programowanie\\GIT_Python\\python\\SPOJ\\Komentarze\\dane.txt'
with open(path, encoding='UTF-8') as plik:
     while True:
        line = plik.readline()
        if line =='': break
        checkLine(line)