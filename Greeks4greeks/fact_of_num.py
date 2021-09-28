#factorial of a number

'''

using loops:-

def fact(n):
    res = 1
    for i in range(2,n+1):
        res=res*i
    return res

n = int(input('Enter a number: '))
print(fact(n))
    
'''
#using recursion:-

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n = int(input('Enter a number: '))
print(fact(n))

