import itertools

kwadraty = [] #zapisujemy, ile mamy 

res = itertools.permutations(range(2,8),5) # budujemy listę podziałów.
for pos in res:
    print(pos)
    ile = 4
    for x in pos:
        ile = (ile-1)+x*x
        if not ile in kwadraty:
            kwadraty.append(ile)
            print('Adding {}'.format(ile))


kwadraty.sort()
print(kwadraty)