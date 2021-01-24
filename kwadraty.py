import itertools

kwadraty = [] #zapisujemy, ile mamy 

def kwad(deep):
    print(deep)
    res = itertools.permutations(range(2,8),deep) # budujemy listę podziałów.
    for pos in res:
        print(pos)
        ile = 4
        for x in pos:
            ile = (ile-1)+x*x
            if not ile in kwadraty:
                kwadraty.append(ile)
                print('Adding {}'.format(ile))

for de in range(1,5):
    kwad(de)

kwadraty.sort()
print(kwadraty)