# Category
Cryptography
# Level
Medium
# Points
100
# Description
```Can you break the one-time multi pad?```
# Files
[encrypt.py](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/OTMP/encrypt.py)</br>
[flag.enc](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/OTMP/flag.enc)
# Solution
We have the flag encrypted at flag.enc also we have the encryption mechanism as at encrypt.py follows
```python
import sys

pt = sys.argv[1]
key = sys.argv[2]

s = list(pt)
for j in xrange(len(key)):
    key = key[1:] + key[:1]
    for i in xrange(len(s)):
        s[i] = chr(ord(s[i]) ^ ord(key[i % len(key)]))

open("flag.enc", "w").write("".join(s))
```
It takes two parameters the first is the flag and the other is the key which is unknown to us</br>
The flag array will be saved at `s`</br>
It will iterate through the the key array and for every iteration it moves the first char at key array to be the last char</br>
Also at every iteration it will loop through the whole flag array xoring it with key array items</br>
Actually at challenges like this, I try to find some vulnerability like some point where some unknown variable can be bruted</br>
This challenge was hard enough to make this from just looking at it or some kind of partial simulations of it</br>
So I decided to get it on a paper and to try it with different small strings and keys</br>
And after some tries I found that for any arbitrary key the result will be just the original chars xored with the whole key chars xored with itself</br>
So if the input (in ascii) is ```102 108 97 103```</br>
And the key (in ascii) is ```107 101 121```</br>
The result (in ascii) will be ```102^(107^101^121) 108^(107^101^121) 97^(107^101^121) 103^(107^101^121)```</br>
So we found our vulnerability !!!</br>
The fact that the value ```107^101^121``` will be constant for all of the chars of the flag allow us to brute it without even knowing the original key</br>
So we can get the flag like this</br>

```python
>>> flag_enc = open('flag.enc','rb').read()
>>> i = 0
>>> while True:
...     flag = ""
...     for ii in flag_enc:
...             flag += chr(ord(ii) ^ i)
...     if "FLAG" in flag:
...             print(flag)
...             break
...     i += 1
...
FLAG{MULT1_PAD_1time_X0RR}
```
# Flag
FLAG{MULT1_PAD_1time_X0RR}
