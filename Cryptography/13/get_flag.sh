#!/bin/bash
./SubstitutionDecoders/caesar.py -d $(cat ./cipherText) -k 13|grep -o picoCTF{.*}

