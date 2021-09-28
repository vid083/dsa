# Find the number of digits in a number

'''
#using loops:-

n = int(input())
count = 0
while n>0:
    count+=1
    n = n//10
print(count)

------------------
# using inbuilt fun:-

num = int(input())
print(len(str(num)))

--------------------

#using recursion:-

def count_digit(n):
    if n==0:
        return 0
    return 1+count_digit(int(n/10)) 

n = int(input('Enter a number: '))
print(count_digit(n))

'''
import math
def count_digit(n):
    return math.floor(math.log(n, 10)+1)

n = int(input())
print(count_digit(n))



