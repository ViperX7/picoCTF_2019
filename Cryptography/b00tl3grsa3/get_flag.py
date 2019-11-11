#!/bin/python3

from primefac import primefac
from Crypto.Util.number import inverse
from gmpy2 import *
from pwn import *
context.log_level = 'critical'

host, port = '2019shell1.picoctf.com', 37874

print('[ + ] Receiving Challange')
conn = remote(host, port)
data = conn.recvall().decode('utf-8')
conn.close()

print('[ + ] Parsing data')
data = data.split('\n')
ciphertext = int(data[0][3:])
n = int(data[1][3:])
e = int(data[2][3:])

print('[ + ] Factorising n...')
factors_of_n = primefac(n)

print('[ + ] Decrypting the ciphertext')
totient = 1

for x in factors_of_n:
    totient *= (x - 1)

d = inverse(e, totient)

decoded = powmod(ciphertext, d, n)
decoded_hex = str(hex(decoded))[2:]

print(bytes.fromhex(decoded_hex).decode('utf-8'))
