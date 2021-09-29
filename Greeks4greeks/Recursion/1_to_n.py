#print numbers from 1 to n using recursion

def fun(n):
    if n>0:
        fun(n-1)
        print(n, '')

n = int(input())
fun(n)
