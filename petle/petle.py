step = 2
value = 1
maxTry = 100

def sort(val):
    arr = [] 
    arr[:0]=str(val)
    arr.sort()
    em =''
    em = em.join(arr)
    return int(em)

def test(step):
    result = []   
    value = 1    
    loop = False
    for counter in range(1,maxTry):
        value *= step
        value = sort(value)
        if value in result:
            result.append(value) # to shop duplicate ;)
            print('Loop detected for step {}, value: {}, set: {}'.format(step, value, result))    
            loop = True
            break
        else:
            result.append(value)

    if not loop:
        #print('Loop not detected for step: {}, number of multiplications {}. Set = {}'.format(step, maxTry, result))                    
        print('Loop NOT detected for step: {}, number of multiplications {}'.format(step, maxTry ))                    
    print('----------------------')   

for x in range(2,30):
    test(x)