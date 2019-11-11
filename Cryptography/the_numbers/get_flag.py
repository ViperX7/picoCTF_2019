#!/bin/env python3

data = [16,9,3,15,3,20,6,'{',20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,'}']
flag = []
for x in data:
    if x in range(0,27):
        flag.append(chr(64+x))
    else:
        flag.append(x)
print("".join(flag),end="")
