#!/bin/python3
encrypted = [ 1096770097,
              1952395366,
              1600270708,
              1601398833,
              1716808014,
              1734293602,
              1701067056,
              892756537]

decoded = ""
          
for x in encrypted:
	decoded += bytes.fromhex(str(hex(x))[2:]).decode('utf-8')
	
print("picoCTF{" + decoded + "}")
	
