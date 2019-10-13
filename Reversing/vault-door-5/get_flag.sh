#!/bin/bash
cipher="JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY0JTYxJTM4JTM4JTMyJTY0JTMwJTMx"
urldecode() { : "${*//+/ }"; echo -e "${_//%/\\x}"; }

encodedURL=$(echo $cipher | base64 -d)
text=$(urldecode $encodedURL)
echo picoCTF{$text}
