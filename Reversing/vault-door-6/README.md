# Vault-Door-6

> Reverse Engineering | 350 Points
-----------------------------

## Problem Statement
>This vault uses an XOR encryption scheme. The source code for this vault is 
here: [VaultDoor6.java](./VaultDoor6.java)
###### HiNT
> * If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.
## Analysis

given that problem tells us that the program uses XOR we can simplly take 
the bytes and XOR them again with the same numberto get the original bytes back.

* [**VaultDoor6.java**](./VaultDoor6.java)
    ```java
        public boolean checkPassword(String password) {
            if (password.length() != 32) {
                return false;
            }
            byte[] passBytes = password.getBytes();
            byte[] myBytes = {
                0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
                0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
                0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
                0xa , 0x63, 0x65, 0x64, 0x67, 0x37, 0x6d, 0x62,
            };
            for (int i=0; i<32; i++) {
                if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
                    return false;
                }
            }
            return true;
        }
    }
    ```


The password is converted to bytes and then XOR is performed between each 
byte and 0x55

## Solution 

0x55  is used to XOR the characters of the string we will do the reverse
> XOR the values in the array with 0x55 and we should get the original
bytes back

* Bytes before XOR
    >        0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
    >        0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
    >        0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
    >        0xa , 0x63, 0x65, 0x64, 0x67, 0x37, 0x6d, 0x62,


* Bytes after XOR operation
    >        0x6e, 0x30, 0x74, 0x5f, 0x6d, 0x55, 0x63, 0x48,
    >        0x5f, 0x68, 0x34, 0x72, 0x44, 0x33, 0x72, 0x5f,
    >        0x74, 0x48, 0x34, 0x6e, 0x5f, 0x78, 0x30, 0x72,
    >        0x5f, 0x36, 0x30, 0x31, 0x32, 0x62, 0x38, 0x37

* Taking them as ASCII value and converting back to characters we get
```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_6012b87}
```

* Here  is a quick [get_flag script](./get_flag.py) showing how to solve this
in python

## FLAG
`picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_6012b87}`
