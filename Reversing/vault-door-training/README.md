# vault-door-training

> Reverse Engineering | 50 Points
-----------------------------

## Problem Statement
>Your mission is to enter Dr. Evil's laboratory and retrieve the blueprints for
his Doomsday Project. The laboratory is protected by a series of locked vault
doors. Each door is controlled by a computer and requires a password to open.
Unfortunately, our undercover agents have not been able to obtain the secret 
passwords for the vault doors, but one of our junior agents obtained the source
code for each vault's computer! You will need to read the source code for each 
level to figure out what the password is for that vault door. As a warmup,
we have created a replica vault in our training facility. The source code for
the training vault is here: [VaultDoorTraining.java](./VaultDoorTraining.java)
###### HINT
> The password is revealed in the program's source code.

## Analysis 
On checking the source code we directly see the flag 

## Solution

* [**VaultDoorTraining.java**](./VaultDoorTraining.java)
    ```java
        // -Minion #9567
        public boolean checkPassword(String password) {
            return password.equals("w4rm1ng_Up_w1tH_jAv4_3b500738c12");
        }
    ```

## Flag
`picoCTF{4rm1ng_Up_w1tH_jAv4_3b500738c12}`
