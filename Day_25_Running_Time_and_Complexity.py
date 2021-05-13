import math
def isPrime(n):
    if n<=1:
        return False
    sqrtn = math.sqrt(n)
    if sqrtn.is_integer():
        return False
    for i in range(2,int(sqrtn)+1):
        if n%i==0:
            return False
    return True
    
numt = int(input())
for i in range(numt):
    n= int(input())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
