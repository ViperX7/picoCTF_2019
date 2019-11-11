#!/bin/python3
'''
---------------------------------------Vigenère cipher---------------------------------------------------
the code is easy to understand just think of alphabets as numbers A-Z => 0-25
all characters are first changet to be  between 0-26
all the operations are performed on these numbers and
then they are translated back to their respective values
----------------------------------------------------------------------------------------------------------
'''

def vigenere_algo(code_char,key_char,mode):       #Algorithm for encrypt/decrypt
    if mode == "decrypt":
        code = 26 - key_char + code_char
    elif mode == "encrypt":
        code = key_char + code_char
    return code


def normalize(char):			          #Make sure that character stays between 0-25
    if char > 25:
        char = char - 26
    elif char < 0:
        char = char * -1 
    return char


def vigenere(code,key,mode):		          #Format handeller function it takes care of 
    flag = []                                     #retaining special characters
    code_length = len(code)                       #uppercase lowercase charccter during input and output
    key_length = len(key)
    key = key.lower()                             #because case of key doesnt matters


    for n in range(code_length):
        code_char = ord( code[n])
        key_char = ord( key[ n % key_length])

        key_char = key_char - 97

        if chr(code_char).isupper() :
            offset = 65
        elif chr(code_char).islower() :
            offset = 97
        else:                                     #Special characters handelling
            key  = (key[key_length-1] + key)[:-1] #key is modified to skip the special characters
            flag.append(chr(code_char))
            continue

        code_char = code_char - offset
        char = vigenere_algo(code_char,key_char,mode)
        char = normalize(char)
        char = char + offset

        flag.append(chr(char))
    return ("".join(flag))


if __name__=="__main__":
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d","--decode",help="Decode text")
    parser.add_argument("-e","--encode",help="Encode text")
    parser.add_argument("-k","--key",help="Key to use for encryption or decryption")
    args = parser.parse_args()

    if args.decode:
        print(vigenere(args.decode,args.key,mode="decrypt"))
    elif args.encode:
        print(vigenere(args.encode,args.key,mode="encrypt"))
