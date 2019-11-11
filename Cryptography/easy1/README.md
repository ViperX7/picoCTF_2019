# Easy1

> Cryptography | 100 Points
-----------------------------

## Problem Statement
>The one time pad can be cryptographically secure, but not when you know the
key.Can you solve this? We've given you the encrypted flag, key, and a table to
help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. Can you use [this](./table.txt)
table to solve it?.
###### HINT
> * Submit your answer in our competition's flag format. For example, if you 
answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
> * Please use all caps for the message.

## Analysis
On looking through the table  and also some experience tells me that it is
**Vigenere Ciphe**r


Vigenere Cipher is just like Caesar cipher the only difference is in caesar
cipher all the alphabets have same shift value but in Vigenere cipher each
alphabet in a word is shifted with different shifts which is determined by the
given key.


## Solution

Or you can use [SubstutionDecoder](https://github.com/ViperX7/SubstitutionDecoders/)
```shell
user@computer:~ ./SubstitutionDecoders/Vigenere_Cipher.py -d UFJKXQZQUNB -i SOLVECRYPTO 
CRYPTOISFUN
```

## Flag 
`picoCTF{CRYPTOISFUN}`

## Resources
* Tool to solve simple substitution ciphers [SubstutionDecoder](https://github.com/ViperX7/SubstitutionDecoders/)
* Online tool for solving Vigenere Cipher [Vigenère Cipher Codebreaker](https://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx)
* See: [Vigenere Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

