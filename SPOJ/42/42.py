import sys

for line in sys.stdin:
    line = line.replace('\n','')
    if line != '42':
    	print(line)	
    else:
  	    break	