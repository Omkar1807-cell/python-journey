def primecheck(a):
    if a <2:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
a = 17
if primecheck(a):
    print("prime number")
else:
    print("not prime")
