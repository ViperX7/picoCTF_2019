# caesar

> Cryptography | 100 Points
-----------------------------

## Problem Statement
>Decrypt this [message](./ciphertext). You can find the ciphertext in
/problems/caesar_0_22aa542fadadcc37b6ec6037c493ec9f on the shell server.


## Solution
Check the result for different shift  on any online decoder 
and see which one gives some readable result

Or you can use [SubstutionDecoder](https://github.com/ViperX7/SubstitutionDecoders/)
```shell
user@computer:~/SubstitutionDecoders/caesar.py -d zolppfkdqeboryfzlktjxksyyl

zolppfkdqeboryfzlktjxksyyl
ynkooejcpdanqxeykjsiwjrxxk
xmjnndiboczmpwdxjirhviqwwj
wlimmchanbylovcwihqguhpvvi
vkhllbgzmaxknubvhgpftgouuh
ujgkkafylzwjmtaugfoesfnttg
tifjjzexkyvilsztfendremssf
sheiiydwjxuhkrysedmcqdlrre
rgdhhxcviwtgjqxrdclbpckqqd
qfcggwbuhvsfipwqcbkaobjppc
pebffvatgurehovpbajznaioob
odaeeuzsftqdgnuoaziymzhnna
nczddtyrespcfmtnzyhxlygmmz
mbyccsxqdrobelsmyxgwkxflly
laxbbrwpcqnadkrlxwfvjwekkx
kzwaaqvobpmzcjqkwveuivdjjw
jyvzzpunaolybipjvudthuciiv
ixuyyotmznkxahoiutcsgtbhhu
hwtxxnslymjwzgnhtsbrfsaggt
gvswwmrkxlivyfmgsraqerzffs
furvvlqjwkhuxelfrqzpdqyeer
etquukpivjgtwdkeqpyocpxddq
dspttjohuifsvcjdpoxnbowccp
crossingtherubiconwmanvbbo
bqnrrhmfsgdqtahbnmvlzmuaan
apmqqglerfcpszgamlukyltzzm

Best Guess:  crossingtherubiconwmanvbbo
```

It will find you the most probable answer automatically
Here's my [Get Flag](./get_flag.sh) script to get the answer quickly


## Flag
`picoCTF{crossingtherubiconwmanvbbo}`


## Resources
* Tool to solve simple substitution ciphers [SubstutionDecoder](https://github.com/ViperX7/SubstitutionDecoders/)
* Online tool for solving caesar cipher [cryptii](https://cryptii.com/pipes/caesar-cipher)
* See: [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
