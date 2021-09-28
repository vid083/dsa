#trailing zeros in factorial of a number

'''
# Naive method:-
'''

def zeros(n):
    fact=1
    for i in range(2,n+1):
        fact = fact*i

        res=0
        while(fact%10==0):
            res+=1
            fact//10
    return res

n = int(input())
print(zeros(n))



