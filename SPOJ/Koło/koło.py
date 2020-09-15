# https://pl.spoj.com/problems/ETI06F1/
import math
import fileinput
#tab = [ '10 10', '1000 1500']

def pole(r, d):
    d = d/2.0
    Rx = math.sqrt(r*r-d*d)
    pi = 3.141592654
    P = pi*Rx*Rx
    print('{:.2f}'.format(P))

for x in fileinput.input():
    pole(float(x.split()[0]), float(x.split()[1]))        

#for x in tab:
#    pole(float(x.split()[0]), float(x.split()[1]))    