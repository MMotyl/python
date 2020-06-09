import re
line = 'participant "Order Tracking DPS-A (HAL)" as OT #lightGreen'
line = 'participant BFF as BFF'
# participant "Shopping Cart DPS-A (HAL)" as SC #lightGreen
# participant "Order Tracking DPS-A (HAL)" as OT #lightGreen
# participant "Payment Management (HAL)" as PM #aqua
line = ' participant "Product Ordering Management (HAL)" as PO #aqua'
# participant Backend as BE

line = line.replace('participant','')
spl = line.split('as')
name  = spl[0].replace('"','')
spl2  = spl[1].split()
alias = spl2[0]

print(line)
print(name, alias)
