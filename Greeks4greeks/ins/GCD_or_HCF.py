#Program to find GCD or HCF of Two Numbers

def computeGCD(x,y):
    while(y):
        x,y = y, x%y
    return x
print(computeGCD(60,48))