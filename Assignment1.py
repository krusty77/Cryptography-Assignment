#!/usr/bin/env python3
import math
import os

# Clearing the Screen
os.system('clear')


print("Question 1")
print("A number p is defined as prime if and only if it is divisible by itself (and 1). Implement a method from scratch that allows to test primality of a number using trial and error method.")
#################################################################################################################################################################################################
flag = True
p_input = ""
p = 0

##Function to get the prime number
def get_prime(p):
    for i in range(2,p):
        if (p%i) == 0:
            return False
    return True

##It will ask for a number until it is prime
while (flag):
    p_input = input("Enter a number: ")
    p = int(p_input)
    os.system('clear')
    print("Answer of Question #1. You entered: " + p_input + "\n")
    if (get_prime(p)==True):
        print("It is a prime number" + "\n")
        flag = False
    else:
        os.system('clear')
        print("It is not a prime number \nYou will need to enter a Prime Number to Continue...")
    

# #
print("Question 2")
print("The technique that you used in the previous question is a bit slow if you consider a big enough number (e.g. 10-digits). Can you think of any other way to improve it? Implement the new one.")
flag = True #Resetting the variables
p_input = ""
p = 0
#################################################################################################################################################################################################
def get_prime_optimized(p):
 for i in range(2,int(math.sqrt(p))+1):
   if (p%i) == 0:
     return False
 return True

while (flag):
    p_input = input("Enter a bigger prime number: ")
    p = int(p_input)
    os.system('clear')
    print("Answer of Question #2. You entered: " + p_input + "\n") 
    if (get_prime_optimized(p)==True):
        print("It is a big prime number " + "\n")
        flag = False
    else:
        print("It is not a big prime number \nYou will need to enter a Prime Number to Continue...")
        os.system('clear')
# #

# #
print("Question 3")
print("Based on the function built in Question 2, implement a function that returns the factorisation of any composite number.")
#################################################################################################################################################################################################
p2_input = input("Enter a composite number: ")
p2 = int(p2_input)
factorization_numbers = []
os.system('clear')

def get_factorization_number(factorization_of_composite):
    for i in range(1,factorization_of_composite+1,1):
        if (factorization_of_composite%i == 0):
            factorization_numbers.append(i)
    return factorization_numbers

print("Answer of Question #3. You entered: " + p2_input + "\n")
if (get_prime_optimized(p2)==False):
   print("It is composite number, see the factorization numbers below: \n")
   print(get_factorization_number(p2))
   factorization_numbers = []
   print("\n")
else:
   print("It is not composite number " + "\n")

# #
print("Question 4")
print("Implement Euclids algorithm and compute a) hcf(499017086208, 676126714752) b) hcf(5988737349, 578354589)")
#################################################################################################################################################################################################
p2_input = input("Enter a number to continue: ")
os.system('clear')
n1 = 499017086208
n2 = 676126714752
n3 = 5988737349
n4 = 578354589

def get_Euclidean_Algorithm(n1, n2):
    if (n1==0):
        return n2,0,1
    gcf,x1,y1 = get_Euclidean_Algorithm(n2%n1,n1)
    #update the numbers
    x = y1 - (n2//n1) *x1
    y = x1

    return gcf,x,y

print("Answer (a): The highest common factor of hcf(499017086208, 676126714752) is: \n")
g,f,c = get_Euclidean_Algorithm(n1,n2)##Assign arbitrary three variables to split the results
print(g)
print("\nAnswer (b):The highest common factor of hcf(5988737349, 578354589) is: \n")
g,f,c = get_Euclidean_Algorithm(n3,n4)##Assign arbitrary variables to split the results
print(g)

# #
print("\nQuestion 5")
print("Explain how Euclids algorithm might help you to find multiplicative inverses and implement it. Solve for x the linear congruence 342952340x=1 mod4230493243")
#################################################################################################################################################################################################
print("\nExplanation: The Euclid Algorithm helps to find multiplicative inverse because for the formula A * A^-1 = 1 mod n, the number A and n must be coprimes\n In other words, if HCF(n1,n2) = 1 we can say they are coprimes and then it will have multiplicative inverse.")

p3_input = input("Enter the first coprime number: ")
os.system('clear')
p4_input = input("Enter the second coprime number: ")
os.system('clear')

def get_linear_congruence(a,b,m):
    x = 0
    y = 0 ##it is not used, just need to capture the value of the function

    ##need to get the value of x and y
    gcf,x,y = get_Euclidean_Algorithm(a,m)

    ##initialize x0
    x0 = (x * (b // gcf)) % m ##used the Python floor division
    result = 0 ##variable to capture the result
    #get the result
    for i in range(gcf):
        result = (x0 + i * (m // gcf)) % m 
    return result

p3 = int(p3_input)
p4 = int(p4_input)
gcf,c,f = get_Euclidean_Algorithm(p3,p4)
if(gcf==1):
    print("The numbers entered: " + p3_input + " and " + p4_input + " have Multiplicative Inverses")
else:
    print("The numbers entered: " + p3_input + " and " + p4_input + " do not have Multiplicative Inverse")

print("The answer for the x in the linear congruence 342952340x=1 mod4230493243 is the following: ")
print(get_linear_congruence(342952340,1,4230493243))
p2_input = input("Enter a number to continue: ")
os.system('clear')


# #
print("Question 6")
print("Write a program to convert an encrypted number c = m^e (mod n) into the original m = c^d (modn), where 0 < m < n is some integer. Pick any plaintext you would like to encrypt using the public key (937513, 638471) and then check the correctness of the algorithm.")
#################################################################################################################################################################################################
n = 937513
e = 638471
p = get_factorization_number(n)[1]
q = get_factorization_number(n)[2]
fn = (p-1)*(q-1)
gcf,c,f = get_Euclidean_Algorithm(fn,e)
d = get_linear_congruence(e,gcf,fn)

def encryption(m):
    return pow(m,e,n) ##Cipher = (Msg)^e mod N

def decryption(c):
    return pow(c,d,n) ##Msg = (Cipher)^d mod N

##Arrays for the cipher and decipher
integer_arrays = [] ##characters converted to number
integer_arrays_encrypted = [] ##characters converted to numbers and encrypted
integer_arrays_unencrypted = [] ##encrypted characters converted to number
final_message_unencrypted = [] ##after encryption this variable should be the same as the original message

original_message = input("Enter a message you want to encrypt: ")##get the message from the user
to_array_original_message = [char for char in original_message] ##original message converted to an array of characters

##Encryption
for i in range (0,len(to_array_original_message)):
    integer_arrays.append(encryption(ord(to_array_original_message[i])))

print("Full Message Encrypted: ")
print(''.join(map(str, integer_arrays)))

##Decryption
for i in range(0,len(integer_arrays)):
    integer_arrays_unencrypted.append(decryption(integer_arrays[i]))
##Message change to characters
for i in range(0,len(integer_arrays_unencrypted)):
    final_message_unencrypted.append(chr(integer_arrays_unencrypted[i]))
##Message
print("Your message derypted is: ")
print("".join(final_message_unencrypted))