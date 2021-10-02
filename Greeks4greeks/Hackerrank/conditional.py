'''
Day 3: Intro to Conditional Statements

Given an integer,n , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Complete the stub code provided in your editor to print whether or not n is weird.

Sample Input 0
3

Sample Output 0
Weird
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    
    if N%2!=0 : 
        print('Weird')
    if N%2==0 :
        if N in range(2,5): 
            print('Not Weird')
        elif N in range(6,21):
            print('Weird')
        elif N>20:
            print('Not Weird')

