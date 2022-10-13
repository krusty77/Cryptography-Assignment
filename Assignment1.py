#!/usr/bin/env python3
import math

print("Question 1")
print("A number p is defined as prime if and only if it is divisible by itself (and 1). Implement a method from scratch that allows to test primality of a number using trial and error method.")
#################################################################################################################################################################################################
p_input = input("Enter a number: ")
p = int(p_input)

def get_prime(p):
    for i in range(2,p):
        if (p%i) == 0:
            return False
    return True

if (get_prime(p)==True):
    print("It is a prime number")
else:
    print("It is not a prime number")

# #
print("Question 2")
print("The technique that you used in the previous question is a bit slow if you consider a big enough number (e.g. 10-digits). Can you think of any other way to improve it? Implement the new one.")
#################################################################################################################################################################################################
p1_user = input("Enter a bigger number: ")
p1 = int(p1_user)
 
def get_prime_optimized(p1):
 for i in range(2,int(math.sqrt(p1))+1):
   if (p1%i) == 0:
     return False
 return True
 
if (get_prime_optimized(p1)==True):
   print("It is a prime number")
else:
   print("It is not a prime number")
# #
