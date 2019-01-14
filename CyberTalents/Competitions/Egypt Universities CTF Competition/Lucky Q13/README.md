# Category
Digital Forensics
# Level
Easy
# Points
50
# Description
```13 is not your lucky number !! think again.```
# File
[QRcode.png](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/Lucky%20Q13/QRcode.png)
# Solution
Using an online QR code decoder like https://zxing.org/w/decode.jspx</br>

The decoded message is</br>
```synt{EBG13_vf_Nj3f0z3!!}```</br>

It's a kind of string rotation</br>
I used http://theblob.org/rot.cgi to get all the rotational possibilities</br>
I found the flag at ROT-13

# Flag
flag{ROT13_is_Aw3s0m3!!}
