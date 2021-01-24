from urle import checkURL

txt = 'https://ubezpieczenia.uniqa.pl/ubezpieczenie-oc/agent/programuniqapartner%C2%A0'
d1, d2 = checkURL(txt)

print(d1)