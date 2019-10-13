#!/bin/python2
secret = [
    106, 85, 53, 116, 95, 52, 95, 98, 0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66,
    0x5f, 0142, 0131, 0164, 063, 0163, 0137, 066, 061, 'e', '0', 'f', '2', '7',
    '6', '9', 'c'
]
flag = []
for x in secret:
    try:
        flag.append(chr(x))
    except:
        flag.append(x)
print('picoCTF{' + ''.join(flag) + '}')
