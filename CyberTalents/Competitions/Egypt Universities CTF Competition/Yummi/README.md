# Category
Cryptography
# Level
Medium
# Points
100
# Description
```
We found the below encrypted secret, can you decrypt it to get the flag. 
WFhHWEdYR1hHWFhYWFhYWFhHR1h7QUFBQkFCQUFCQV8yREZGRERERERGRkRERkRERERERERGRERERkZERkZEREZGRkRAV1ZWVldXVlZWV1dWV1ZWVldXV1YwTk1NTU1OTU1OTX0=
```
# Solution
First I decoded it as base64 and I got this</br>
```
XXGXGXGXGXXXXXXXXGGX{AAABABAABA_2DFFDDDDDFFDDFDDDDDDDFDDDFFDFFDDFFFD@WVVVWWVVVWWVWVVVWWWV0NMMMMNMMNM}
```
This is a kind of 2-char cipher for the parts `XXGXGXGXGXXXXXXXXGGX`, `AAABABAABA`, `DFFDDDDDFFDDFDDDDDDDFDDDFFDFFDDFFFD`, `WVVVWWVVVWWVWVVVWWWV`, `NMMMMNMMNM`</br>
Searching for `2 chars cipher` got me to this https://puzzling.stackexchange.com/questions/5905/what-characteristics-of-a-ciphertext-can-be-indicators-of-a-particular-cipher</br>
It contains</br>
```
A Bacon cipher is composed of 2 binary bits, which can be represented by anything (eg. could be upper/lowercase as in one recent question, or could be based on whether a cat is white/black, as seen in another). The tell-tale sign is if the ciphertext length is divisible by 5, as each letter requires 5 binary bits of Bacon. Yum.
```
Which really fits for our encrypted flag</br>
Now we use https://www.dcode.fr/bacon-cipher to decrypt all parts one by one</br>
# Flag
FLAG{2CT_2NDEASYP@SSWP0RT}
