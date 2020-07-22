import fileinput
#tab = [ '1. KowalSki JaCEk', '2. mazurkiewicz pIoTR', '3. prokoP ANna', '4. MisioL annA', '5. BerezOwSki jaCEK', '6. pietraS ANNA', '7. WILkowsKA aneta']

res = {}

for poz in fileinput.input():
    skladowe = poz.upper().split(' ')
    imie = skladowe[2]
    if imie in res:
        res[imie] = res[imie]+1
    else:
        res[imie] = 1

#parsing results

sort = sorted(res.values(), reverse = True)
unique_values = list(dict.fromkeys(sort))

for i in unique_values: 
    theSame = [k for k,v in res.items() if v==i]
    theSame.sort()
    for pos in theSame:
        print (pos, i) 

# https://pl.spoj.com/problems/NAMES/