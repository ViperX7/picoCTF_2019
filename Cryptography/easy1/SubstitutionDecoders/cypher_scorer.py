#!/bin/env python3

alphabets = {
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0,
    "E": 0,
    "F": 0,
    "G": 0,
    "H": 0,
    "I": 0,
    "J": 0,
    "K": 0,
    "L": 0,
    "M": 0,
    "N": 0,
    "O": 0,
    "P": 0,
    "Q": 0,
    "R": 0,
    "S": 0,
    "T": 0,
    "U": 0,
    "V": 0,
    "W": 0,
    "X": 0,
    "Y": 0,
    "Z": 0
}
alpha = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
ENGLISH_FREQS = [
    0.08167,
    0.01492,
    0.02782,
    0.04253,
    0.12702,
    0.02228,
    0.02015,
    0.06094,
    0.06966,
    0.00153,
    0.00772,
    0.04025,
    0.02406,
    0.06749,
    0.07507,
    0.01929,
    0.00095,
    0.05987,
    0.06327,
    0.09056,
    0.02758,
    0.00978,
    0.02360,
    0.00150,
    0.01974,
    0.00074,
]


def calc_score(string, freq=ENGLISH_FREQS):
    # Function to calculate frequency of letters from a given piece of text
    sum = 0
    string = string.lower()
    for char in string:
        if char not in alpha:  # Special characters handelling
            continue
        sum = sum + (ENGLISH_FREQS[ord(char) - 97])
    return sum


def annalyse_freq(string):
    n = 0
    for char in string:
        n = n + 1
        if char.isalpha():
            char = char.upper()
            alphabets[char] = (alphabets[char] + 1)
    data = []
    for x in alphabets:
        data.append(alphabets[x] / n)
    return data


if __name__ == "__main__":
    print(calc_score(input()))
