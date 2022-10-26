#!/usr/bin/env python3
import math
import os

factorization_numbers = []
def get_factorization_number(factorization_of_composite):
    for i in range(1,factorization_of_composite+1,1):
        if (factorization_of_composite%i == 0):
            factorization_numbers.append(i)
    return factorization_numbers

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

e = 937513
n = 638471
p = get_factorization_number(n)[1]
q = get_factorization_number(n)[2]
fn = (p-1)*(q-1)
gcf,c,f = get_Euclidean_Algorithm(fn,e)
d = get_linear_congruence(e,gcf,fn)

def encryption(m):
    return pow(m,e,n) ##Cipher = (Msg)^e mod N

def decryption(c):
    return pow(c,d,n) ##Msg = (Cipher)^d mod N

test = "Me cago en Lonnis"

to_array = [char for char in test]
integer_arrays = []
integer_arrays_unencrypted = []
teste = []
test2 = []

print(to_array)

print("raw")
for i in range (0,len(to_array)):
    integer_arrays.append(encryption(ord(to_array[i])))
    teste.append(ord(to_array[i]))

print(teste)

print("Message Encrypted: ")
for i in range(0,len(integer_arrays)):
    print(integer_arrays[i])

print("Message Unencrypted: ")
for i in range(0,len(integer_arrays)):
    integer_arrays_unencrypted.append(decryption(integer_arrays[i]))
print(integer_arrays_unencrypted)

for i in range(0,len(integer_arrays_unencrypted)):
    test2.append(chr(integer_arrays_unencrypted[i]))

print("Message Converted to String: ")
print(test2)

print("Full Message Encrypted: ")
print(''.join(map(str, integer_arrays)))

print("Your message was: ")
print("".join(test2))