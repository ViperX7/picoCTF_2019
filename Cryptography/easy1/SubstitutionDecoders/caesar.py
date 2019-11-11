#!/bin/env python3
import os
'''
-----------------------------------Caesaar chipper-------------------------------------------------
the code is easy to understand just think of alphabets as numbers A-Z => 0-25
all characters are first changet to be  between 0-26
all the operations are performed on these numbers and
then they are translated back to their respective values
--------------------------------------------------------------------------------------------------------
'''
import os


def caesar_algo(code, key, mode):  # Algorithm for encrypt/decrypt
    if mode == "decrypt":
        code = code - key
    elif mode == "encrypt":
        code = code + key
    return code


def normalize(char):  # Make sure that character stays between 0-25
    if char >= 26:
        char = char - 26
    elif char < 0:
        char = char + 26
    return char

def extended_normalizer(char):
    if char <= 32:
        char = char + 126 - 32
    elif char > 126:
        char = char - 126 + 32
    return char


def extended_normalizer1(char):
    if char <= 34:
        char = char + 126 - 34
    elif char > 126:
        char = char - 126 + 34
    return char


def extended_normalizer2(char):
    if char < 0:
        char = char + 256
    elif char >= 256:
        char = char - 256
    return char


def extended_normalizer3(char):
    if char <= 31:
        char = char + 128
    elif char > 128:
        char = char - 128 + 31
    return char


def caesar(secret, key, mode, method):
    result = []
    if method == "normal":
        key = key % 26
    elif method == "extended":
        key = key % 256
    if method == "normal":
        for char in secret:
            if char.isupper():
                offset = 65
            elif char.islower():
                offset = 97
            else:  # Special characters handelling

                result.append(char)
                continue

            char = ord(char)  # Convert character to number
            char = char - offset  # bring it between 0-25
            char = caesar_algo(char, key, mode)
            char = normalize(char)
            char = char + offset  # again send it to it's respective domain
            result.append(chr(char))
    elif method == "extended":
        for char in secret:
            # if char in [" ", "!",'"']:          #pseudo code from previous version
            #     result.append(char)
            #     continue
            char = ord(char)
            char = caesar_algo(char, key, mode)
            char = extended_normalizer(char)
            result.append(chr(char))
    elif method == "extended3":
        for char in secret:
            char = ord(char)
            char = caesar_algo(char, key, mode)
            char = extended_normalizer3(char)
            result.append(chr(char))



    return "".join(result)


def decode(secret, method):
    import cypher_scorer
    entpb = []
    flags = []
    if method == "extended":
        size = 128
    elif method == "normal":
        size = 26
    for ofset in range(size):
        result = caesar(secret, ofset, mode="decrypt", method=method)
        score = cypher_scorer.calc_score(result)
        flags.append(result)
        entpb.append(score)
    i = 0
    mx = max(entpb)
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

    parser.add_argument(
        "-d",
        "--decode",
        help=
        "Try to decode with(out) key useful if the encoded string has some meaning"
    )
    parser.add_argument("-e", "--encode", help="Encode with the given key")
    parser.add_argument("-k", "--key", type=int, help="Supply the key")
    parser.add_argument(
        "-m",
        "--method",
        help=
        "Option to specify encoding/decoding in extended or normal or custom modes default is normal"
    )

    args = parser.parse_args()
    if args.method:
        method = args.method
    else:
        method = "normal"
    if args.encode:
        if args.key:
            print(caesar(args.encode, args.key, mode="encrypt", method=method))
        else:
            print("Secret: " +
                  caesar(args.encode,
                         int(input("Enter an Integer Key(0-25): ")),
                         mode="encrypt",
                         method=method))
    if args.decode:
        if args.key:
            print(caesar(args.decode, args.key, "decrypt", method=method))
        else:
            decode(args.decode, method=method)
