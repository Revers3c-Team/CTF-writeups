# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
Not Available
# File
[ezez_keygen](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/MIU%20CTF%20Competition/ezez%20keygen/ezez_keygen)
# Solution
The file is x64 stripped linux binary</br>
Running it gave me this</br>

```sh
$ ./ezez_keygen
usage: ./easy_keygen username serial
$ ./ezez_keygen plapla plapla
unrecognized user
$
```

The main function looks like this</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/MIU%20CTF%20Competition/ezez%20keygen/img1.PNG)

Which does this</br>
1) Make sure the number of arguments is at least 2</br>
2) Two checks; The first argument is `4dminUser31337` and `sub_4008B9(argv[1],argv[2])` returns 1</br>
3) If passed them it will print the flag to be `argv[2]`

So we now know that the username should be `4dminUser31337` and the serial should be the flag</br>
Our target now is to make `sub_4008B9(username,serial)` return 1; decompiling it ...</br>

```c++
signed __int64 __fastcall sub_4008B9(const char *a1, const char *a2)
{
  signed __int64 result; // rax
  char *v3; // rax
  size_t v4; // [rsp+10h] [rbp-10h]
  size_t v5; // [rsp+18h] [rbp-8h]

  v4 = strlen(a1);
  v5 = strlen(a2);
  if ( v4 > 0x1E || v5 > 0x64 )
    return 0xFFFFFFFFLL;
  if ( ((0xAAAAAAAAAAAAAAABLL * v5 >> 64) >> 1) + v5 - 3 * ((0xAAAAAAAAAAAAAAABLL * v5 >> 64) >> 1) != v4 )
    return 0xFFFFFFFFLL;
  v3 = sub_400746(a2);
  if ( !strcmp(v3, a1) )
    result = 1LL;
  else
    result = 0xFFFFFFFFLL;
  return result;
}
```

Which does this</br>
1) Make two checks on lengths of username and serial</br>
2) If `sub_400746(serial)` equals `4dminUser31337` it will return 1</br>

Because we know the length of the username, we can brute for the length of the serial</br>

```python
>>> v4 = len('4dminUser31337')
>>> for i in range(0x64):
...  if ((0xAAAAAAAAAAAAAAAB * i >> 64) >> 1) + i - 3 * ((0xAAAAAAAAAAAAAAAB * i >> 64) >> 1) == v4: print(i)
...
38
40
42
>>>
```

Now our target is to make `sub_400746(serial)` return `4dminUser31337`</br>
I also decompiled it to be</br>

```c++
char *__fastcall sub_400746(const char *a1)
{
  char v2; // [rsp+14h] [rbp-5Ch]
  int i; // [rsp+18h] [rbp-58h]
  char nptr[2]; // [rsp+20h] [rbp-50h]
  char v5; // [rsp+22h] [rbp-4Eh]
  char v6[8]; // [rsp+30h] [rbp-40h]
  __int64 v7; // [rsp+38h] [rbp-38h]
  __int64 v8; // [rsp+40h] [rbp-30h]
  __int64 v9; // [rsp+48h] [rbp-28h]
  unsigned __int64 v10; // [rsp+58h] [rbp-18h]

  v10 = __readfsqword(0x28u);
  *v6 = 0LL;
  v7 = 0LL;
  v8 = 0LL;
  v9 = 0LL;
  *nptr = 0;
  v5 = 0;
  for ( i = 0; i < strlen(a1); i += 3 )
  {
    if ( a1[i + 2] != 45 && a1[i + 2] != 43 )
    {
      puts("Invalid serial format!");
      exit(-1);
    }
    v2 = 0;
    if ( a1[i + 2] == 43 )
      v2 = 1;
    nptr[0] = a1[i];
    nptr[1] = a1[i + 1];
    v5 = 0;
    v6[i / 3] = 2 * strtol(nptr, 0LL, 16) + v2;
  }
  return strdup(v6);
}
```

Which does this</br>
1) Loop through the serial at chunks with length 3 for each one</br>
2) At every chunk it does this</br>
a) Make sure the third char is `+` or `-`</br>
b) `v2` will be 0 when the third char is `-` and 1 if it's `+`</br>
c) Puts the first and the second char at the two-char-chunk `nptr`</br>
d) Decode `nptr` as hex (`strtol(nptr,0,16)` in c looks like `int(nptr,16)` in python), multiply it by 2 and add the result to `v2`</br>
c) The result will be appended to `v6` that will returned after that</br>

For this we know that the output should be `4dminUser31337`</br>
So this is how I solved it</br>
1) Loop through chars of `4dminUser31337`</br>
2) At every char check if the ascii code is odd, if so, decrease it by 1</br>
3) Divide the result by 2 and get its hex value</br>
4) Append `-` if we decreased it and `+` if not</br>

```python
>>> ret = ""
>>> for i in list('4dminUser31337'):
...   ch = ord(i)
...   if ch % 2 == 0:
...    kind = "-"
...   else:
...    kind = "+"
...    ch = ch - 1
...   ch = ch / 2
...   ret += hex(ch)[2:]+kind
...
>>> print("flag{%s}" % ret)
flag{1a-32-36+34+37-2a+39+32+39-19+18+19+19+1b+}
>>>
```

And because upper-case hex is just decoded like lower-case hex we have this</br>

```sh
# ./ezez_keygen 4dminUser31337 1a-32-36+34+37-2a+39+32+39-19+18+19+19+1b+
flag is: flag{1a-32-36+34+37-2a+39+32+39-19+18+19+19+1b+}
# ./ezez_keygen 4dminUser31337 1A-32-36+34+37-2A+39+32+39-19+18+19+19+1B+
flag is: flag{1A-32-36+34+37-2A+39+32+39-19+18+19+19+1B+}
#
```

So the flag may be upper or lower case (I didn't have the chance to submit it)

# Flag
flag{1A-32-36+34+37-2A+39+32+39-19+18+19+19+1B+}
