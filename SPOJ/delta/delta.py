# https://pl.spoj.com/problems/ROWNANIE/
import fileinput

def delta(a, b, c):
    de = b*b - 4*a*c
    return de

for x in fileinput.input():
    de = delta(float(x.split()[0]), float(x.split()[1]), float(x.split()[2]))
    if de  >0: print('2') 
    if de ==0: print('1') 
    if de  <0: print('0') 