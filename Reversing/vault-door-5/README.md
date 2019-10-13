# Vault-Door-5

> Reverse Engineering | 300 Points
-----------------------------

## Problem Statement
>In the last challenge, you mastered octal (base 8), decimal (base 10), and
hexadecimal (base 16) numbers, but this vault door uses a different change of
base as well as URL encoding!
The source code for this vault is here: [VaultDoor5.java](./VaultDoor5.java)
###### HINT
> * You may find an encoder/decoder tool helpful, such as https://encoding.tools/
> * Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

## Analysis 
The Source code performs base64 and urlencodingi on the supplied password and 
then compare it with a stored value

* [**VaultDoor5.java**](./VaultDoor5.java)
    ```java
        public boolean checkPassword(String password) {
            String urlEncoded = urlEncode(password.getBytes());
            String base64Encoded = base64Encode(urlEncoded.getBytes());
            String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                            + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                            + "JTM0JTVmJTY0JTYxJTM4JTM4JTMyJTY0JTMwJTMx";
            return base64Encoded.equals(expected);
        }
    }
    ```


## Solution

* The Given String
    >JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY0JTYxJTM4JTM4JTMyJTY0JTMwJTMx


* Firstly we will decode the expected string using base64 [Online base64Encoded](https://www.base64decode.org/)

    >%63%30%6e%76%33%72%74%31%6e%67%5f%66%72%30%6d%5f%62%61%35%65%5f%36%34%5f%64%61%38%38%32%64%30%31

* Now we will urldecode this string that we obtained in previous step 
[Online urlencoder](https://www.urlencoder.org/)
    >picoCTF{c0nv3rt1ng_fr0m_ba5e_64_da882d01}



Here is a quick [Get_Flag Script](./get_flag.sh)

## Flag
`picoCTF{c0nv3rt1ng_fr0m_ba5e_64_da882d01}`


## Resources

[How to urldecode using shell ](https://stackoverflow.com/questions/6250698/how-to-decode-url-encoded-string-in-shell)

