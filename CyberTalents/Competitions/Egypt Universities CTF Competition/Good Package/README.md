# Category
Malware Reverse Engineering
# Level
Easy
# Points
50
# Description
```This is not a good package```
# File
[simple.exe](https://github.com/Revers3c-Team/CTF-writeups/blob/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/Good%20Package/simple.exe)
# Solution
The file is 32 bit windows binary compiled with the debugging information</br>
So we load it into IDA</br>

The main function

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/Good%20Package/img1.PNG)

Actully the flag value is dynamically initialized as shown</br>
To convert any hex value to ascii string in python</br>
```python
>>> print("67616C66".decode('hex')[::-1])
flag
```

So we have our flag
# Flag
flag{B4sics_4r3_ManDat0ry}
