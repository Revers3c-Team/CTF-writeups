# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
`Only a plaintext password would be easier...`
# File
[simple_reverse](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Helwan%20University%20CTF%20Competition/simple%20reverse/simple_reverse)
# Solution
The file is x64 non-stripped linux binary, so I loaded it to IDA</br>
For the main function we have</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Helwan%20University%20CTF%20Competition/simple%20reverse/img1.PNG)

It requires an input, then it checks it with `check_password`, and it should return zero to print the flag</br>
So I'm going to reverse this function to get the right password</br>

```c++
signed __int64 __fastcall check_password(const char *a1)
{
  signed int i; // [rsp+18h] [rbp-28h]
  __int64 v3; // [rsp+20h] [rbp-20h]
  __int64 v4; // [rsp+28h] [rbp-18h]
  __int16 v5; // [rsp+30h] [rbp-10h]
  unsigned __int64 v6; // [rsp+38h] [rbp-8h]

  v6 = __readfsqword(0x28u);
  v3 = -5480071635338481426LL;
  v4 = -5482867658982444575LL;
  v5 = 242;
  if ( strlen(a1) != 17 )
    return 0xFFFFFFFFLL;
  for ( i = 0; i <= 16; ++i )
  {
    if ( *(&v3 + i) != (a1[i] ^ 0x80) )
      return 0xFFFFFFFFLL;
  }
  return 0LL;
}
```

We have some important points here</br>
1) The password length has to be 17
2) `*(&v3 + i)` is `&v3[i]`</br>
3) We have an array pointer `&v3` that can be converted to list using this python snippet

```python
# run with python2
def signed_int_to_bytes(signed_int,size):
  # Little-endian
  string = hex(signed_int & (2**(8*size)-1))
  string = string.replace('L','').replace('0x','')
  if len(string) % 2:
   string = '0' + string
  string = string.decode('hex')
  string = string[::-1]
  return string

v3 = []
v3 += signed_int_to_bytes(-5480071635338481426,8)
v3 += signed_int_to_bytes(-5482867658982444575,8)
v3 += signed_int_to_bytes(242,8)
print(v3)
```

So it will be `['\xee', '\xb0', '\xf4', '\xdf', '\xe1', '\xdf', '\xf2', '\xb3', '\xe1', '\xb1', '\xdf', '\xe3', '\xe9', '\xf0', '\xe8', '\xb3', '\xf2']`</br>

To get the password</br>

```python
>>> v3 = ['\xee', '\xb0', '\xf4', '\xdf', '\xe1', '\xdf', '\xf2', '\xb3', '\xe1', '\xb1', '\xdf', '\xe3', '\xe9', '\xf0', '\xe8', '\xb3', '\xf2']
>>> password = ""
>>> for i in v3:
...  password += chr(ord(i) ^ 0x80)
...
>>> print(password)
n0t_a_r3a1_ciph3r
```

Now use it to get the flag</br>

# Flag
flag{xor_is_pretty_simple}

