lista = 'https://www.abc.pl/?asd=2'
lista2 = 'https://www.abc.pl/'

def host(url):
   pos = url.find('/?') #usunięcie paramsów 
   if pos !=-1:
      url = url[:pos]
   
   if url[-1] =='/':  # usunięcie slasha
      url = url[:len(url)-1]
   print(url)       

host(lista)   
host(lista2)   

-------------------------
from urllib.parse import urlparse

x = urlparse('https://www.cwi.nl:80/%7Eguido/Python.html?par1=23&par2=dupa')
print(x.scheme, x.hostname, x.path, x.query)

lista = 'https://www.abc.pl/?asd=2'
lista2 = 'https://www.abc.pl/'

x = urlparse(lista)
print(x)
x = urlparse(lista2)
print(x)

-------------------------
dic = {"x": 7, "txt": "opis"}
txt = dic.get('y',0)
print (txt)