# Category
Cryptography
# Level
Easy
# Points
50
# Description
```
one form of string representations is readable but the other is not. can you read the flag. 
102108097103123067084095049115116069097115121083051099114051116051080064115115112104114052053051125 Flag format is FLAG{XXXXXXXXXX}
```
# Solution
If we devided it into 3-char chunks it will be</br>
```103 108 097 103 ...```

Which seem to be ascii values of some chars</br>
So we can convert it with python</br>

```python
>>> flag = ""
>>> ascii = "102108097103123067084095049115116069097115121083051099114051116051080064115115112104114052053051125"
>>> for i in xrange(0,len(ascii),3):
...    flag += chr(int(ascii[i:i+3]))
...
>>> print(flag)
flag{CT_1stEasyS3cr3t3P@ssphr453}
```

# Flag
flag{CT_1stEasyS3cr3t3P@ssphr453}
