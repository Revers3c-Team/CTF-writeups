# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
Not Available
# File
[a.out](https://github.com/Revers3c-Team/CTF-writeups/blob/master/CyberTalents/Competitions/CyberTeam%20Company%20Internship%20CTF/Say%20my%20Name/a.out)
# Solution
The file is x86 non-stripped linux binary</br>
Let's load it into IDA</br>
Also I renamed some variables based on its functionality</br>
For the main function</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/CyberTeam%20Company%20Internship%20CTF/Say%20my%20Name/img1.PNG)

Which reads from the stdin two names `firstname` and `secondname` with limit of 7 chars only</br>
After that it starts a loop as follows</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/CyberTeam%20Company%20Internship%20CTF/Say%20my%20Name/img2.PNG)

It's so obvious that it loops from 0 to 6 (7 iterations) and at every iteration it will xor a char from `firstname` with its index-equivalent char from `secondname` and stores the result at `s1` array
Let's continue</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/CyberTeam%20Company%20Internship%20CTF/Say%20my%20Name/img3.PNG)

At this point it checks if the array `s1` equals the array `unk_97F`</br>
`unk_97F`'s address is 0x97F (as ida names unknown memory pointers with their addresses)</br>
I dumped the value of this array (I need only 7 bytes) using idapython api with this command</br>
```python
>>> print([GetManyBytes(0x97F,7)])
['\x05\x1d\r\x04\x10r\x00']
```
After that it will decode the flag and print it</br>

So we have two ways:</br>
1) Debug it and change the flow to the start of the decryption loop and set s1 array to `\x05\x1d\r\x04\x10r\x00`</br>
2) Just figure out any two strings that if xored with each other will generate this array

I used the second way, so I made this simple python script</br>
```python
>>> import subprocess
>>> str1 = 'plapla1'
>>> arr = '\x05\x1d\r\x04\x10r\x00'
>>> str2 = ''.join(chr(ord(str1[i]) ^ ord(arr[i])) for i in range(7))
>>> process = subprocess.Popen(["./a.out"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
>>> process.stdin.write(str1+str2)
>>> print(process.communicate()[0])
Please enter your first name:
Please enter your last name:
Hello Boss, Here's your flag:
FLAG{SO_MANY_XORS}
```
# Flag
FLAG{SO_MANY_XORS}
