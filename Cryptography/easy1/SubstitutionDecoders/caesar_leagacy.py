#!/bin/env python3
'''
----------------------------------------Caesaar chipper-------------------------------------------------
the code is easy to understand just think of alphabets as numbers A-Z => 0-25
all characters are first changet to be  between 0-26
all the operations are performed on these numbers and
then they are translated back to their respective values
--------------------------------------------------------------------------------------------------------
'''
import math
import os


#the below values are used to guess the key when no decryption key is provided
ENGLISH_FREQS = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406,
                 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974,0.00074,]


def caesar_algo(code,key,mode):                         #Algorithm for encrypt/decrypt
    if mode == "decrypt":
        code = code - key
    elif mode =="encrypt":
        code = code + key
    return code



def normalize(char):                                    #Make sure that character stays between 0-25
    if char >=26:
        char = char - 26
    elif char < 0:
        char = char + 26
    return char

def Kore(secret):
    skip = 0
    secreat = secret.lower()
    for char in secret:
        if char.isalpha():                                          #Special characters handelling
            result.append(char)
            skip = skip + 1
            continue
        sum = sum + math.log(ENGLISH_FREQS[char-97])
    entpb = (-1 * sum / math.log(2) / (len(secret)-skip))
    return entpb



def caesar(secret, key, mode, guess=False):
    result = []
    sum = 0
    skip = 0
    key = key % 26
    for char in secret:

        if char.isupper():
            offset = 65
        elif char.islower():
            offset = 97

        else :                                          #Special characters handelling
            result.append(char)
            skip = skip + 1
            continue

        char = ord(char)                                   #Convert character to number
        char = char - offset                            #bring it between 0-25
        char = caesar_algo(char,key,mode)
        char = normalize(char)
        char = char + offset                            #again send it to it's respective domain
        result.append(chr(char))


        if guess==True:                                 #Scooring
            sum = sum + math.log(ENGLISH_FREQS[char-offset])
    if guess == True:
        entpb = (-1 * sum / math.log(2) / (len(secret)-skip))
        return ["".join(result),str(entpb)]
    else:
        return "".join(result)


def decode(secret):
    entpb = []
    flags =  []
    for ofset in range(26):
        result,score = caesar(secret,ofset,mode="decrypt", guess=True)
        flags.append(result)
        entpb.append(score)
    i = 0
    mx = min(entpb)
    for x in entpb:
        if x == mx:
            break
        i = i + 1
    for flag in flags:
        print(flag)
    print("\nBest Guess: ", flags[i])




if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--decode", help="Try to decode with(out) key useful if the encoded string has some meaning")
    parser.add_argument("-e", "--encode", help = "Encode with the given key")
    parser.add_argument("-k", "--key",type=int, help="Supply the key")

    args = parser.parse_args()

    if args.encode:
        if args.key:
            print(caesar(args.encode,args.key,mode = "encrypt"))
        else:
            print("Secret: " + caesar(args.encode, int(input("Enter an Integer Key(0-25): ")),mode = "encrypt"))


    if args.decode:
        if args.key:
            print(caesar(args.decode,args.key,"decrypt"))
        else:
            decode(args.decode)




