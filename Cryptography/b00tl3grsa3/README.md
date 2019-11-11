# b00tl3gRSA3

> Cryptography | 450 Points
-----------------------------

## Problem Statement
>Why use p and q when I can use more? Connect with nc 2019shell1.picoctf.com 37874.
###### HINT
>There's more prime factors than p and q, finding d is going to be different.

## Analysis

As the question suggest more than two prime numbers have been used to calculate
n we can say that n has a number of factors

In any RSA encryptino if we can find all factors (generally p and q) we can break the encryption here
in this problem we need to find all the factors of n

> The only difference that occour in calculation of totient and n

> For Example let there be five prime numbers p,q,r,s,t then
> the totient will be calculated as
>
>
    n = p * q * r * s * t
    totient = (p - 1) * (q - 1) * (r - 1) * (s - 1) * (t - 1)


Rest of the process will continue normally

## Solution
Generally to find the factors of a number factordb is a GOTO site but sometimes
it fails and yes it failed for me this time it gave some factors fut they were
incorrect.

There is also a python module [primefac](https://github.com/elliptic-shiho/primefac-fork) that we can use to factorise n.

Here is my [Get flag](./get_flag.py) script


## Flag
`picoCTF{too_many_fact0rs_0744041}`

## Resources
* [Encryption using more than two primes](https://crypto.stackexchange.com/questions/44110/rsa-with-3-primes)
* Online factorisation tool [factordb](http://factordb.com/)
* Utility to factor large numbers [primefac](https://github.com/elliptic-shiho/primefac-fork)
    >```pip install primefac-fork```

