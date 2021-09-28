# sum of first 'n' natural numbers

'''
using formula:- efficient method

def getsum(n):
    return n*(n+1)/2

n = int(input())
print(getsum(n))

-------------------

using loops:- ----> not excuted

def getsum(n):
    sum = 0
    for i in range(n):
        sum = sum+i
    return sum

n = int(input())
print(getsum(n))
'''

#using recursion:-

def getsum(n):
    if (n<=0):
        return 0
    else:
        return n+getsum(n-1) 

n = int(input())
print(getsum(n))