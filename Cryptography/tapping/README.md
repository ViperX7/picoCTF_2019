# Tapping

> Cryptography | 200 Points
-----------------------------

## Problem Statement
> Theres tapping coming in from the wires. What's it saying nc 2019shell1.picoctf.com 37920.
###### HINT
> * What kind of encoding uses dashes and dots?
> * The flag is in the format PICOCTF{}



## Analysis
When we connect to the given addresss we get the following output


```shell
viperx7@computer:~/ nc 2019shell1.picoctf.com 37920
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- ---.. .---- ---.. ..--- ..--- ....- ..... --... ..... } 
```

The output contains dots and dashes we can quickly guess that the output is
morse code.



## Flag
`picoctf{m0rs3c0d31sfun1818224575}`


## Resources
* Online Tool to decode morse code [unit-conversion.info](http://www.unit-conversion.info/texttools/morse-code/)
