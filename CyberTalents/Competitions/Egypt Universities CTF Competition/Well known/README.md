# Category
Cryptography
# Level
Easy
# Points
50
# Description
```
given the value: 6mup8c336ww32ck561gkgr9q61jkcrhjcrwk6t356gtk2cv66dhg Get the flag, it's pretty simple. Flag format flag{XXXXXXX}
```
# Solution
I tried to decode it as base64 and it didn't work so I tried base32 and it worked</br>
I decoded it at https://www.browserling.com/tools/base32-decode and the result is `55d0c7812e0a8a70e6b2f93de4313f3c`</br>
It's md5 hash so I used https://hashkiller.co.uk/md5-decrypter.aspx to decrypt it</br>
# Flag
notsecure
