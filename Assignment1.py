#!/usr/bin/env python3
import math
import os

# Clearing the Screen
os.system('clear')


print("Question 1")
print("A number p is defined as prime if and only if it is divisible by itself (and 1). Implement a method from scratch that allows to test primality of a number using trial and error method.")
#################################################################################################################################################################################################
p_input = input("Enter a number: ")
p = int(p_input)
os.system('clear')

def get_prime(p):
    for i in range(2,p):
        if (p%i) == 0:
            return False
    return True

print("Answer of Question #1. You entered: " + p_input + "\n")
if (get_prime(p)==True):
    print("It is a prime number" + "\n")
else:
    print("It is not a prime number " + "\n")

# #
print("Question 2")
print("The technique that you used in the previous question is a bit slow if you consider a big enough number (e.g. 10-digits). Can you think of any other way to improve it? Implement the new one.")
#################################################################################################################################################################################################
p1_input = input("Enter a bigger prime number: ")
p1 = int(p1_input)
os.system('clear')
 
def get_prime_optimized(p1):
 for i in range(2,int(math.sqrt(p1))+1):
   if (p1%i) == 0:
     return False
 return True

print("Answer of Question #2. You entered: " + p1_input + "\n") 
if (get_prime_optimized(p1)==True):
   print("It is a prime number " + "\n")
else:
   print("It is not a prime number " + "\n")
# #

# #
print("Question 3")
print("Based on the function built in Question 2, implement a function that returns the factorisation of any composite number.")
#################################################################################################################################################################################################
p2_input = input("Enter a composite number: ")
p2 = int(p2_input)
factorization_numbers = []
os.system('clear')

def get_factorization_number(p2):
    for i in range(1,p2+1,1):
        if (p2%i == 0):
            factorization_numbers.append(i)
    return factorization_numbers

print("Answer of Question #3. You entered: " + p2_input + "\n")
if (get_prime_optimized(p2)==False):
   print("It is composite number, see the factorization numbers below: \n")
   print(get_factorization_number(p2))
   print("\n")
else:
   print("It is not composite number " + "\n")

# #
print("Question 4")
print("Implement Euclids algorithm and compute a) hcf(499017086208, 676126714752) b) hcf(5988737349, 578354589)")
#################################################################################################################################################################################################
p2_input = input("Enter a number to continue: ")
n1 = 499017086208
n2 = 676126714752
n3 = 5988737349
n4 = 578354589

def get_hcf(n1, n2):
    if (n1==0):
        return n2
    else:
        return get_hcf(n2%n1,n1)

print("The highest common factor of hcf(499017086208, 676126714752) is: \n")
print(get_hcf(n1,n2))
print("\nThe highest common factor of hcf(5988737349, 578354589) is: \n")
print(get_hcf(n2,n4))

# #
print("Question 5")
print("Explain how Euclids algorithm might help you to find multiplicative inverses and implement it. Solve for x the linear congruence 342952340x=1 mod4230493243")
#################################################################################################################################################################################################
