import fileinput
def cezar(txt):
    wynik =''
    for lit in txt:
        if ord(lit)>31:
            if lit != ' ':
                zn = ord(lit)-65
                zn = (zn+3)%26
                l2 = chr(zn+65)
            else:
                l2 = ' '    
            wynik += l2    
    return wynik

for line in fileinput.input():
    wyn = cezar(line)
    print(wyn)
