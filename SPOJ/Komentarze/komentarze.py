# https://pl.spoj.com/problems/BFNTEST/
import fileinput
groupComment = False

def checkLine(line):
    global groupComment
    tmpComment = False
    line = line.replace('\n','')
    if not groupComment and (line.find('/*')!= -1):
        groupComment = True
        print(line.split('/*')[0])
    if groupComment & (line.find('*/')!= -1):
        groupComment = False
        tmpComment = True        
    if (line.find('*/')!= -1 ) and (line.find('/*')!= -1):
        tmpComment = True
        print('')
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