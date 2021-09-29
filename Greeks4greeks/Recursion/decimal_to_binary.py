# Decimal to binary conversion:-

def fun(n):
    if n>0:
        fun(n//2)
        print(n%2)

n=int(input())
fun(n)