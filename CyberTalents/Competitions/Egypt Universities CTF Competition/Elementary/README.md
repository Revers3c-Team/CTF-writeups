# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
```Here we've prepared a simple program, crack me if you can.```
# File
[Elementary](https://raw.githubusercontent.com/Revers3c-Team/CTF-writeups/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/Elementary/elementary)
# Solution
First we binary architecture with `file` command
```
$ file elementary
ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d39e86cbb1ab3d21df90dda89aa7c1b27465d613, stripped
```
So it's x64 stripped linux binary</br>
We load it with IDA and modify the variables names</br>
The main function</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/Elementary/img1.PNG)

From that we understand that it will read from stdin into two pointers username and password</br>
After that it will pass the two pointers as arguments to func1 and further checks for the return status code stored at `eax`</br>

The func1 function

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/Elementary/img2.PNG)

It's obvious that it will check the password if it equals `N1C3Tryy` and prints `nice!` if so overlooking the username</br>
So we got our flag</br>
# Flag
N1C3Tryy
