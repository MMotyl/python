from collections import OrderedDict

fileName = "E:\Programowanie\GIT\HAL\HAL-core\public\sequenceDiagrams\SalesCheckout\BillingCheckout_v2.puml"
with open(fileName) as plik:
    lines = plik.readlines()

result = OrderedDict() # serwer i operacja

for line in lines:
    pos = line.find(">")
    if pos>0:
        elementy = line.partition(":")
        #print("line "+line.replace("\n",""))

        metoda = elementy[2].replace("\n","")
        serwer = elementy[0].partition(">")
        serwis = serwer[2].replace("\n","")

        #print("method: "+metoda)
        #print ("server: "+serwis)
        #print ("--------")

        elem = {}
        elem["server"] = serwis
        elem["method"] = metoda

        result.append(elem)

def add(se, me):
    pozycja = {}
    for i in result.items:
        if i["serwer"] == se:
            pozycja =i
    if pozycja=={}:
        pozycja["server"] = se
        pozycja["method"] = me
        result.append(pozycja)
    else: 

# wynik
for el in result:
    print(el)
#    print(el[0])
#    print(el[1])