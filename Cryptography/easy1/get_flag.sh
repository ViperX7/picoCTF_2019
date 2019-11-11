#!/bin/bash
echo -n picoCTF{ && echo -n $(./SubstitutionDecoders/Vigenere_Cipher.py -d $(cat cipherText) -k $(cat key)) &&echo }
