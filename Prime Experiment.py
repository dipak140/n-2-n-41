# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 10:46:11 2019

@author: Dipak Kumar
"""
n = 0

def print_factors(x):
   count = 0
   # This function takes a number and prints the factors
   #print("The factors of",x,"are:")
   for j in range(1, x + 1):
       if x % j == 0:
           count += 1
   return count

i = 1
while i==1:
    P = (n**2) + (n + 41)
    count = print_factors(P)
    if count == 2:
        print("{0} is a prime number".format(P))
    if count > 2:
        print("{0} is not a prime number for n={1}".format(P,n))
        break
    n = n+1