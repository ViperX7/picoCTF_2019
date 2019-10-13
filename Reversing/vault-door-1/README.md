# Vault-Door-1

> Reverse Engineering | 100 Points
-----------------------------

## Problem Statement
>This vault uses some complicated arrays! I hope you can make sense of it
special agent. The source code for this vault is here: [VaultDoor1.java](./VaultDoor1.java)
###### HINT
> * Look up the charAt() method online.

## Analysis
A particular part of the given program looks interesting

* **[VaultDoor1.java](./VaultDoor1.java)**
    ```java
        public boolean checkPassword(String password) {
            return password.length() == 32 &&
                   password.charAt(0)  == 'd' &&
                   password.charAt(29) == '7' &&
                   password.charAt(4)  == 'r' &&
                   password.charAt(2)  == '5' &&
                   password.charAt(23) == 'r' &&
                   password.charAt(3)  == 'c' &&
                   password.charAt(17) == '4' &&
                   password.charAt(1)  == '3' &&
                   password.charAt(7)  == 'b' &&
                   password.charAt(10) == '_' &&
                   password.charAt(5)  == '4' &&
                   password.charAt(9)  == '3' &&
                   password.charAt(11) == 't' &&
                   password.charAt(15) == 'c' &&
                   password.charAt(8)  == 'l' &&
                   password.charAt(12) == 'H' &&
                   password.charAt(20) == 'c' &&
                   password.charAt(14) == '_' &&
                   password.charAt(6)  == 'm' &&
                   password.charAt(24) == '5' &&
                   password.charAt(18) == 'r' &&
                   password.charAt(13) == '3' &&
                   password.charAt(19) == '4' &&
                   password.charAt(21) == 'T' &&
                   password.charAt(16) == 'H' &&
                   password.charAt(27) == '1' &&
                   password.charAt(30) == 'f' &&
                   password.charAt(25) == '_' &&
                   password.charAt(22) == '3' &&
                   password.charAt(28) == 'e' &&
                   password.charAt(26) == '5' &&
                   password.charAt(31) == 'd';
        }
    }
    ```

We can clearly see that the program checks each character of the password
one by one and that too in random order

## Solution

There are two ways to get the flag 

* **The Booring way** by reordering the lines of the given source file
    ```java
        public boolean checkPassword(String password) {
            return password.length() == 32 &&
                   password.charAt(0)  == 'd' &&
                   password.charAt(1)  == '3' &&
                   password.charAt(2)  == '5' &&
                   password.charAt(3)  == 'c' &&
                   password.charAt(4)  == 'r' &&
                   password.charAt(5)  == '4' &&
                   password.charAt(6)  == 'm' &&
                   password.charAt(7)  == 'b' &&
                   password.charAt(8)  == 'l' &&
                   password.charAt(9)  == '3' &&
                   password.charAt(10) == '_' &&
                   password.charAt(11) == 't' &&
                   password.charAt(12) == 'H' &&
                   password.charAt(13) == '3' &&
                   password.charAt(14) == '_' &&
                   password.charAt(15) == 'c' &&
                   password.charAt(16) == 'H' &&
                   password.charAt(17) == '4' &&
                   password.charAt(18) == 'r' &&
                   password.charAt(19) == '4' &&
                   password.charAt(20) == 'c' &&
                   password.charAt(21) == 'T' &&
                   password.charAt(22) == '3' &&
                   password.charAt(23) == 'r' &&
                   password.charAt(24) == '5' &&
                   password.charAt(25) == '_' &&
                   password.charAt(26) == '5' &&
                   password.charAt(27) == '1' &&
                   password.charAt(28) == 'e' &&
                   password.charAt(29) == '7' &&
                   password.charAt(30) == 'f' &&
                   password.charAt(31) == 'd';
        }
    }
    ```


    > Now once we have ordered the lines passwords can easily be seen

* **The Hackish way:** Check this script out  [get_flag.sh](./get_flag.sh)

## Flag

`picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_51e7fd}`



