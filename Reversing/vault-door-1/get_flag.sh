#!/bin/bash
echo -n picoCTF{
for x in {0..33}
do 
    echo -n $(cat VaultDoor1.java |grep -e \($x\)|cut -d "'" -f2)
done
echo  }
