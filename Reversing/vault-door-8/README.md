# Vault-Door-8

> Reverse Engineering | 450 Points
-----------------------------

## Problem Statement
>Apparently Dr. Evil's minions knew that our agency was making copies of their
source code, because they intentionally sabotaged this source code in order to
make it harder for our agents to analyze and crack into! The result is a quite 
mess, but I trust that my best special agent will find a way to solve it.
The source code for this vault is here: [VaultDoor8.java](./VaultDoor8.java)
###### HINT
> * Clean up the source code so that you can read it and understand what is going on.
> * Draw a diagram to illustrate which bits are being switched in the scramble() method, 
then figure out a sequence of bit switches to undo it.
You should be able to reuse the switchBits() method as is.

## Analysis
On looking at the code we can observe that entire code has been minified
(all formating ,indentation) are removed making the code extreamly jard to read.

First we need to make our code readable 
Now our Code looks like [**VaultDoor8_beautified.java**](./VaultDoor8_beautified.java)

* The function that we are intrested in
    >```java
    > public char[] scramble(String password) {
    >  /* Scramble a password by transposing pairs of bits. */
    >  char[] a = password.toCharArray();
    >  for (int b = 0; b < a.length; b++) {
    >   char c = a[b];
    >   c = switchBits(c, 1, 2);
    >   c = switchBits(c, 0, 3); /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */
    >   c = switchBits(c, 5, 6);
    >   c = switchBits(c, 4, 7);
    >   c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
    >   c = switchBits(c, 3, 4);
    >   c = switchBits(c, 2, 5);
    >   c = switchBits(c, 6, 7);
    >   a[b] = c;
    >  }
    >```




    >This particular function on a higher level does the following
    >* Takes a string and split it into characters
    >* These characters are then converted integers
    >* Finally each integer is converted into binary 
    >* Then bits of the binary number are shuffeled in a particular order
    >* That results in a new number.
    >* This new number is then compared to stored values in the program


* This one checks  password and has all the stored values

    >```java
    > public boolean checkPassword(String password) {
    >  char[] scrambled = scramble(password);
    >  char[] expected = { 0xF4,0xC0,0x97,0xF0,0x77,0x97,0xC0,0xE4,0xF0,0x77,0xA4,0xD0,
    >                      0xC5,0x77,0xF4,0x86,0xD0,0xA5,0x45,0x96,0x27,0xB5,0x77,0xE1,
    >                      0xC0,0xA4,0x95,0x94,0xD1,0x95,0x94,0xD0 };
    >  return Arrays.equals(scrambled, expected);
    >```

## Solution


We will do each step in reverse
* **Step 1:** Take the value 
* **Step 2:** Convert to binary
* **Step 3:** Swap its bits in appropriate order
* **Step 4:** Convert the binary back to number
    > For example the given program switches 6th and 7th index last
    > but we will need to switch it firsti and then second last adn so on..
* **Step 5:** Convert then number to a ASCII equivalent

We need to do these five steps for every stored value in the checkPassword
function


Here is my [Get Flag script](./get_flag.py)

## Flag
`picoCTF{s0m3_m0r3_b1t_sh1fTiNg_60bea5ea1}`



## Resources
Online Java Beautier  [codebeautify.org](https://codebeautify.org/javaviewer)

















