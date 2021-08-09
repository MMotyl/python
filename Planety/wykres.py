import math
import matplotlib.pyplot as plt 


res = []
  
for i in range(0,360*40):
    a = math.sin(math.radians(i/3))
    b = math.sin(math.radians(i/4))
    c = math.sin(math.radians(i/5))

#    a = math.sin((i/3))
#    b = math.sin((i/4))
#    c = math.sin((i/5))
    txt = ("{0};{1:.6f};{2:.6f};{3:.6f}".format(i, a, b,c))
    res.append(txt)
            
    if math.isclose(a, b, abs_tol=1e-2):
        # print ("{3}:{4}  a[{0:.6f}] close to b[{1:.6f}]".format(a,b,i,i/360))        
        # print ("{0}:{4} => a[{1:.6f}] b[{2:.6f}] c[{3:.6f}] ".format(i, a, b,c, i/360))                
        if math.isclose(b, c, abs_tol=1e-2):
            print ("!!!!! {0} => a[{1:.6f}] b[{2:.6f}] c[{3:.6f}] ".format(i, a, b,c))        
 
with open('D:\\Programowanie\\GIT_Python\\python\\Planety\\planety2.csv', 'w') as fp:
    fp.write('i;x;y;z\n')  
    for line in res:
        fp.write(line+'\n')
