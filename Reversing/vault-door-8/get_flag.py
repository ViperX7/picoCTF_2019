#!/bin/python3

# Function to convert decimal numbers to binary
def dec2bin(x):
    binary = []
    rev=[]
    while(x>0):
        binary.append(x%2)
        x=x//2
    binary.reverse()
    for x in binary:
        rev.append(str(x))
    return ''.join(rev)


# function to convert binary to decimal
def bin2dec(inp):
	inp = str(inp)
        dec = 0
	for x in range(0,len(inp)):
		dec += pow(2,x) * int(inp[len(inp)-x-1])
	return dec

# function to switch bits 
def switchBits(b,n,m):
    while(len(b) < 8):
        b = ['0'] + b
        b[n],b[m] = b[m],b[n]
        return b


#array with data
arr = [ 0xF4,0xC0,0x97,0xF0,0x77,0x97,0xC0,0xE4,0xF0,0x77,0xA4,0xD0,
        0xC5,0x77,0xF4,0x86,0xD0,0xA5,0x45,0x96,0x27,0xB5,0x77,0xE1,
        0xC0,0xA4,0x95,0x94,0xD1,0x95,0x94,0xD0 ]


### Refference Code from challenge
'''
   c = switchBits(c, 1, 2);
   c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
   c = switchBits(c, 5, 6);
   c = switchBits(c, 4, 7);
   c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
   c = switchBits(c, 3, 4);
   c = switchBits(c, 2, 5);
   c = switchBits(c, 6, 7);
'''

#SwitchingBits in reverse order
#The code segment below switch the bits in reverse order
result = ""
for x in arr:
	binary = dec2bin(x)
	unit = []
	for y in binary :
		unit.append(y)
	unit = switchBits(unit,6,7)
	unit = switchBits(unit,2,5)
	unit = switchBits(unit,3,4)
	unit = switchBits(unit,0,1)
	unit = switchBits(unit,4,7)
	unit = switchBits(unit,5,6)
	unit = switchBits(unit,0,3)
	unit = switchBits(unit,1,2)
	
	res += chr(bin2dec(unit))

print('picoCTF{' + res + '}')
