wojewodztwa = ('dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie', 'małopolskie', 'mazowieckie',
'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie', 'świętokrzyskie', 'warmińsko-mazurskie', 'wielkopolskie',
'zachodniopomorskie')
wojSet = []

for w in wojewodztwa:   
    pos = {'wojewodztwo':w, 'min':'', 'minLen':0, 'max': '' , 'maxLen':0,  'set': set(w) }
    wojSet.append( pos )

path = 'D:\\Programowanie\\GIT_Python\\python\\slowa\odm.txt'

debug = True

def sprSlowo(slowo, pos):
    global wojSet
    sloLen = len(slowo)
    krotsz = sloLen < wojSet[pos]['minLen']
    dlozszy = sloLen > wojSet[pos]['maxLen']
    if not(krotsz or dlozszy):
            return
    sl = set(slowo)
    if (sl & wojSet[pos]['set']) == set():
        if wojSet[pos]['max'] == wojSet[pos]['min'] == '':
            wojSet[pos]['max'] = slowo
            wojSet[pos]['maxLen'] = sloLen
            wojSet[pos]['min'] = slowo
            wojSet[pos]['minLen'] = sloLen

        if dlozszy:
            wojSet[pos]['max'] = slowo
            wojSet[pos]['maxLen'] = sloLen
        else:            
            wojSet[pos]['min'] = slowo
            wojSet[pos]['minLen'] = sloLen
        if debug:    
            print('{} | {} , {}'.format(wojSet[pos]['wojewodztwo'], wojSet[pos]['min'], wojSet[pos]['max']))


with open(path, encoding='UTF-8') as plik:
     while True:
        line = plik.readline()
        line = line.rstrip()
        if not line :
            break;
        for slowo in line.split(','):
            slowo = slowo.replace(' ','').lower()
            for x in range(len(wojSet)):
                sprSlowo(slowo,x)

print('-----------------------------------')
for pos in wojSet:
    print('{}\t| najkrótsze:{} [{}] \tnajdłuższe {} [{}]'.format(pos['wojewodztwo'], pos['min'],pos['minLen'], pos['max'], pos['maxLen']))