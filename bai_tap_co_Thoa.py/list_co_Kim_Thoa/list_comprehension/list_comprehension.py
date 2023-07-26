import random
L = [random.randint(1,100) for i in range(50)] 
L1 = [ i*i for i in L]

dem = 0
L2 = [ i for i in L if i > 50]
print(len(L2))