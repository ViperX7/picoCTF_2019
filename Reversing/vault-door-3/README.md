# Vault-Door-3

> Reverse Engineering | 200 Points
-----------------------------

## Problem Statement
>This vault uses for-loops and byte arrays. The source code for this vault is 
here: [VaultDoor3.java](./VaultDoor3.java)
###### HINT
> * Make a table that contains each value of the loop variables and the
corresponding buffer index that it writes to.

## Analysis

There is only the checkPassword function is of our intrest

* [**VaultDoor3.java**](./VaultDoor3.java)
    ```java
            public boolean checkPassword(String password) {
            if (password.length() != 32) {
                return false;
            }
            char[] buffer = new char[32];
            int i;
            for (i=0; i<8; i++) {
                buffer[i] = password.charAt(i);
            }
            for (; i<16; i++) {
                buffer[i] = password.charAt(23-i);
            }
            for (; i<32; i+=2) {
                buffer[i] = password.charAt(46-i);
            }
            for (i=31; i>=17; i-=2) {
                    buffer[i] = password.charAt(i);
                }
                String s = new String(buffer);
                return s.equals("jU5t_a_sna_3lpm11ga4e_u_4_m9rf48");
            }
    }
    ```


It runs through various loops and scrambles the password and finaly
matches that scrambled password with a stored value.


## Solution

To solve this we have to Literally Reverse what the program is doing
we will run same number loops for same conditions but we will exchange 
the place of password and buffer variable with eachother


Check This **[Get Flag](./get_flag.py)** script to see how can we reverse the 
scrambled password

## Flag
`picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e9af18}` 
