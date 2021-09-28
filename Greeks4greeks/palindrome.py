n = int(input())    
rev = 0
temp = n
while(temp != 0):
        last = temp % 10  #last digit
        rev = rev*10+last
        temp = temp//10   #remaining digit
if (rev == n):
    print(n,'is a palidrome')
else:
    print(n,'is not a palidrome')
