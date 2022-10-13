# Cryptography-Assignment

## The RSA Algorithm

The RSA algorithm belongs to the family of public key encryption algorithms and stands for Ron
Rivest, Adi Shamir and Leonard Adleman, who first publicly described it in 1978. A user of RSA
creates and then publishes the product of two large prime numbers, along with an auxiliary
value, as their public key. The prime factors must be kept secret.

Anyone can use the public key to encrypt a message, but with currently published methods, if
the public key is large enough, only someone with knowledge of the prime factors can feasibly
decode the message. This construction improves upon the complexity introduced in case of
using symmetric encryption algorithms as the parties that wish to communicate have to share a
priori the public keys. This complexity of key management grows quadratic in terms of the
number of participants in a network.