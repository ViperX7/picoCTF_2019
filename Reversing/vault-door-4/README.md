# Vault-Door-4

> Reverse Engineering | 250 Points
-----------------------------

## Problem Statement
>This vault uses ASCII encoding for the password. The source code for this vault
is here: [VaultDoor4.java](./VaultDoor4.java)
###### HINT
> * Use a search engine to find an "ASCII table".
> * You will also need to know the difference between octal, decimal, and hexademical numbers.

## Analysis

The Secret variable seems to contain what we need, lets see

* **[VaultDoor4.java](./VaultDoor4.java)**
    ```java
        public boolean checkPassword(String password) {
            byte[] passBytes = password.getBytes();
            byte[] myBytes = {
                106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
                0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
                0142, 0131, 0164, 063 , 0163, 0137, 066 , 061 ,
                'e' , '0' , 'f' , '2' , '7' , '6' , '9' , 'c' ,
            };
            for (int i=0; i<32; i++) {
                if (passBytes[i] != myBytes[i]) {
                    return false;
                }
            }
            return true;
        }
    }
    ```


It seems like all the values in the array secret lies between 0-128 
ie the ASCII range it might be our flag.


## Solution 
We will convert each element to a printable character and then print all of 
them together

In python the program to do so will look like:
```python
secret = [  106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 066 , 061 ,
            'e' , '0' , 'f' , '2' , '7' , '6' , '9' , 'c' ]
            
for x in secret:
    try:
        print(chr(x),end='')
    except:
        print(x,end='')
```


Here is  how to I did it [Get_Flag](./get_flag.py)

## Flag
`picoCTF{jU5t_4_bUnCh_0f_bYt3s_61e0f2769c}`
