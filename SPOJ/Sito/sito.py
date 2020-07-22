import fileinput
import math
from datetime import datetime

max_size = 100000
tab_pier = [True] * (max_size+1)
tab_pier[0] = False
tab_pier[1] = False


rng = int(math.sqrt(max_size)) # pierwiastek z max_size
for ind in range(2,rng):
    if tab_pier[ind]:
        for ind2 in range(ind*ind,max_size,ind):
            tab_pier[ind2] = False



firstLine = True
for line in fileinput.input():
    x = int(line)
    if firstLine:
        firstLine = False
    else:    
        if tab_pier[x]:
            print('TAK')
        else:
            print('NIE')
