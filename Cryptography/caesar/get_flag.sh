#!/bin/bash
echo -n picoCTF{ && echo -n $(./SubstitutionDecoders/caesar.py -d $(cat ciphertext)|tail -n 5|head -n 1|cut -d "{" -f2)

