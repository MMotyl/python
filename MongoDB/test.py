from distutils.log import error
import re

try:
    expr = re.compile("^.*Achaja.*", re.IGNORECASE)  # compile the regex
except:
    print(error())    
    
myquery = { "name": expr} # wersja prosta
print (expr)
print(myquery)