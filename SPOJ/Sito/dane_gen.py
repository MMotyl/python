import math
print(2)
for num in range(3,100000,2):
    if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
        print (num)