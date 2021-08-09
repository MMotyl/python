import math
 

a = 0.0011
b = 0.0022

print(math.isclose(a, b, rel_tol=0.01) )


print(math.isclose(2.005, 2.005, rel_tol=0.01))
print(math.isclose(2.005, 2.004, rel_tol=0.01))
print(math.isclose(2.006, 2.005, rel_tol=0.01))    
print(math.isclose(-0.000000234234,-0.00000034243))
print(math.isclose(-0.000000234234,-0.00000034243, rel_tol=0.01))
print(math.isclose(-0.000000234234,-0.00000034243, abs_tol=0.01))