wojewodztwa = ('dolnośląskie', 'kujawsko-pomorskie', 'lubelskie', 'lubuskie', 'łódzkie', 'małopolskie', 'mazowieckie',
'opolskie', 'podkarpackie', 'podlaskie', 'pomorskie', 'śląskie', 'świętokrzyskie', 'warmińsko-mazurskie', 'wielkopolskie',
'zachodniopomorskie')
wojSet = []

for w in wojewodztwa:   
    pos = {'nazwa':w, 'set':set(w)}
    wojSet.append( pos )

def niedopas(slowo):
    sl = set(slowo)
    wynik = []
    for woj in wojSet:
        res = woj['set'] & sl
        # print(res)
        if res ==set():
            wynik.append(woj['nazwa'])

    return wynik

winner = '' # wygrywający wyraz
wojWoj = [] # wygrywające województwo

path = 'D:\\Programowanie\\GIT_Python\\python\\slowa\odm.txt'

with open(path, encoding='UTF-8') as plik:
     while True:
        line = plik.readline()
        line = line.rstrip()
        if not line :
            break;
        for slowo in line.split(','):
            slowo = slowo.replace(' ','').lower()
            if len(slowo)> len(winner):
                wynik = niedopas(slowo)
                if len(wynik) >0:
                    wojWoj = wynik
                    winner = slowo
                    print('{} -> {}'.format(slowo, ','.join(wojWoj) ))
