# 13

> Cryptography | 100 Points
-----------------------------

## Problem Statement
>Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
###### HINT
> This can be solved online if you don't want to do it by hand!


## Analysis
ROT13 cipher moves every character of the string to 13 places
>ie . A => N,
>     B => O and so on...
>
>Since there are total 26 letters in english alphabet
>applying ROT13 two times on the same string gives back the original string.
>That means same algorithm can be used to encode and decode the message.


## Solution 
Use any rot13 decoder to solve this problem
Check the result for shift = 13 on some online tool like
[this](https://cryptii.com/pipes/caesar-cipher)


Or you can use [SubstutionDecoder](https://github.com/ViperX7/SubstitutionDecoders/)
on running it with -k 13 it will give off the flag

```shell
user@computer:~/SubstitutionDecoders/caesar.py -d cvpbPGS{abg_gbb_onq_bs_n_ceboyrz} -k 13
picoctf{not_too_bad_of_a_problem}
```


Here is my [**Get Flag**](./get_flag.sh) script

## Flag
`picoctf{not_too_bad_of_a_problem}`

## Resources
* Utility to solve basic substution problems [SubstutionDecoder](https://github.com/ViperX7/SubstitutionDecoders/)
* Wikipedia :[ROT13](https://en.wikipedia.org/wiki/ROT13)
