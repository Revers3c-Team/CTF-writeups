# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
training, keep training.
# File
[training](https://github.com/Revers3c-Team/CTF-writeups/blob/master/CyberTalents/Competitions/Ahram%20Canadian%20University%20CTF%20Competition/Training/training)
# Solution
The file is a x64 stripped linux binary</br>
At running, it reads from stdin and just prints back what I write</br>
So let's load it to IDA</br>
I also used HexRays decompiler to get the pseudo-code of the functions</br>
For the main function we have</br>

```c++
__int64 __fastcall main(__int64 a1, char **a2, char **a3)
{
  _QWORD *v3; // rax
  char v4; // bl
  __int64 v5; // rax
  char v7; // [rsp+Fh] [rbp-A1h]
  char v8; // [rsp+10h] [rbp-A0h]
  char v9; // [rsp+30h] [rbp-80h]
  char v10; // [rsp+50h] [rbp-60h]
  char v11; // [rsp+70h] [rbp-40h]
  unsigned __int64 v12; // [rsp+98h] [rbp-18h]

  v12 = __readfsqword(0x28u);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(&v8, a2, a3);
  sub_130A();
  while ( 1 )
  {
    v3 = std::operator>><char,std::char_traits<char>,std::allocator<char>>(&std::cin, &v8);
    if ( !std::basic_ios<char,std::char_traits<char>>::operator bool(v3 + *(*v3 - 24LL)) )
      break;
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(&v9, &v8);
    sub_13DB(&v10, &v9);
    v4 = 0;
    if ( sub_1A6C(&v10, &unk_2046A0) )
    {
      std::allocator<char>::allocator(&v7);
      v4 = 1;
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(&v11, "correct", &v7);
    }
    else
    {
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(&v11, &v8);
    }
    v5 = std::operator<<<char,std::char_traits<char>,std::allocator<char>>(&std::cout, &v11);
    std::ostream::operator<<(v5, &std::endl<char,std::char_traits<char>>);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(&v11);
    if ( v4 )
      std::allocator<char>::~allocator(&v7);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(&v10);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(&v9);
  }
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(&v8);
  return 0LL;
}
```

Here we have a C++ program, so we have other functions to allocate memory and copy data</br>
For now we can understand 
```c++
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
``` 
to be a data copy mechanism that copies the data from the second parameter to the first one</br>
And
```c++
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
```
to be a memory free mechanism</br>
First let me explain the code line by line</br>
1) First it defines the different used variables and their types</br>
2) Assigns `v12` to be a 8-byte (qword) address at offset 0x28 from the register segment FS (not important for us)</br>
3) `a2` and `a3` are the parameters of the main function so this should be a default operation (not important for us)</br>
4) Executes the function `sub_130A`
5) Initiates an infinity loop (can be broken from inside)
6) Copies the address of pointer `v8` to the address of the stdin (now any input data will be at pointer `v8`)
7) Checks if the previous operation returned properly if not it will break (not important for us)
8) Copies the address of `v8` to the address of `v9` (now any input data will be at pointer `v9`)
9) Executes sub_13DB with two pointers `v10` and `v9` (our input data)
10) Assigns `v4` to be 0
11) Executes `sub_1A6C` with two pointer `&v10` and unknown pointer at 0x2046A0 and check for the return
12) If returned a non-zero value it allocates some memory and gives its address to pointer `v7` and assigns `v4` to 1
13) Copies the string `correct` to memory of `v11`
14) If returned zero, it copies data from `v8` (our input data) to pointer `v11`
15) Copies address of `v11` (`correct` or our input data) to be the address of stdout (prints `&v11`)
16) Prints new line
17) Free memory of `v11`
18) Free memory of `v7` if `v4` is non-zero (or when the previous condition is true)
19) Free memory of `v9`, `v10`, `v8`, and return

So simply it will read our input, make some check on it, if it passed it will print 'correct' if not it will print our input</br>
For the checking function `sub_1A6C` we have

```c++
_BOOL8 __fastcall sub_1A6C(__int64 a1, __int64 a2)
{
  __int64 v2; // rbx
  __int64 v3; // r12
  __int64 v4; // rbx
  __int64 v5; // rax
  _BOOL8 result; // rax

  v2 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size(a1);
  result = 0;
  if ( v2 == std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size(a2) )
  {
    v3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size(a1);
    v4 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::data(a2);
    v5 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::data(a1);
    if ( !sub_18BF(v5, v4, v3) )
      result = 1;
  }
  return result;
}
```

And for `sub_18BF`

```c++
int __fastcall sub_18BF(const void *a1, const void *a2, size_t a3)
{
  int result; // eax

  if ( a3 )
    result = memcmp(a1, a2, a3);
  else
    result = 0;
  return result;
}
```

Which seems to be a simple comparison function that makes sure the data and the size of the two pointers are the same</br>
So now we need to know the data at the pointer `unk_2046A0`, but when I tried to dump it it was not initialised</br>
Pointer `unk_2046A0` will be initialised at the runtime by some function</br>
To know where it will be filled with data in ida you can jump to its x-refernces (right click-->jump to xref)</br>
To find that it will be initialised by the function `sub_178E` at which we have

```c++
unsigned __int64 __fastcall sub_178E(int a1, int a2)
{
  char v3; // [rsp+17h] [rbp-19h]
  unsigned __int64 v4; // [rsp+18h] [rbp-18h]

  v4 = __readfsqword(0x28u);
  if ( a1 == 1 && a2 == 0xFFFF )
  {
    std::ios_base::Init::Init(&unk_204680);
    __cxa_atexit(&std::ios_base::Init::~Init, &unk_204680, &off_204008);
    std::allocator<char>::allocator(&v3);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(
      &unk_2046A0,
      "IQHR}nxio_vtvk_aapbijsr_vnxwbbmm{",
      &v3);
    std::allocator<char>::~allocator(&v3);
    __cxa_atexit(
      &std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string,
      &unk_2046A0,
      &off_204008);
    sub_19B4(&unk_204260);
    __cxa_atexit(sub_261E, &unk_204260, &off_204008);
  }
  return __readfsqword(0x28u) ^ v4;
}
```

From the code we know that it will copy the string `IQHR}nxio_vtvk_aapbijsr_vnxwbbmm{` to our unknown pointer</br>
Now I am pretty sure that the function `sub_13DB` is the encryption function that takes two pointers `&v10` and `&v9` (our input) and it will encrypt our input and copy the result to `&v10` to be checked again by `sub_1A6C`</br>
Now for `sub_13DB` we have

```c++
__int64 __fastcall sub_13DB(__int64 a1, __int64 a2)
{
  int v2; // ebx
  char *v3; // rax
  signed int v4; // eax
  char *v5; // rax
  char *v6; // rax
  __int64 v7; // rbx
  int i; // [rsp+14h] [rbp-1Ch]
  int v10; // [rsp+18h] [rbp-18h]

  for ( i = 0; *std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i); ++i )
  {
    v2 = *std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i);
    v10 = v2 + *sub_1A4C(&unk_204260, i);
    v3 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i);
    if ( sub_1929(*v3) )
    {
      v4 = 122;
    }
    else
    {
      v5 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i);
      if ( sub_194C(*v5) )
        v4 = 90;
      else
        v4 = *std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i);
    }
    while ( v10 > v4 )
      v10 -= 26;
    if ( *std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i) == 123 )
    {
      LOBYTE(v7) = 125;
    }
    else if ( *std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i) == 125 )
    {
      LOBYTE(v7) = 123;
    }
    else
    {
      v6 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i);
      if ( sub_18FA(*v6) )
        LOBYTE(v7) = v10;
      else
        v7 = *std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i);
    }
    *std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i) = v7;
  }
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(a1, a2);
  return a1;
}
```

You can understand
```c++
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](a2, i)
```
to be just `(&a2+i)` which is `a2[i]`</br>

For `sub_1A4C`, `sub_1929`, `sub_194C`, `sub_18FA`, they are just small checking functions</br>

Also we have this pointer `unk_204260` which is also not initialised, jump to its x-references to find out the function that will fill it </br>
This function is `sub_130A` which is hard to be reversed so we will debug (source code debugging) it to get the data at this pointer</br>
I set a break point at the line after the line it used in</br>
I used ida x64 remote linux debugger server on ubuntu x64</br>
Dumped the data from it with `GetManyBytes` idapython api function</br>
The dumped data was
`['\x03\x00\x00\x00\x05\x00\x00\x00\x07\x00\x00\x00\x0b\x00\x00\x00\r\x00\x00\x00\x11\x00\x00\x00\x13\x00\x00\x00\x17\x00\x00\x00\x1d\x00\x00\x00\x1f\x00\x00\x00%\x00\x00\x00)\x00\x00\x00+\x00\x00\x00/\x00\x00\x005\x00\x00\x00;\x00\x00\x00=\x00\x00\x00C\x00\x00\x00G\x00\x00\x00I\x00\x00\x00O\x00\x00\x00S\x00\x00\x00Y\x00\x00\x00a\x00\x00\x00e\x00\x00\x00g\x00\x00\x00k\x00\x00\x00m\x00\x00\x00q\x00\x00\x00\x7f\x00\x00\x00\x83\x00\x00\x00\x89\x00\x00\x00\x8b\x00\x00\x00\x95\x00\x00\x00\x97\x00\x00\x00\x9d\x00\x00\x00\xa3\x00\x00\x00\xa7\x00\x00\x00\xad\x00\x00\x00\xb3\x00\x00\x00\xb5\x00\x00\x00\xbf\x00\x00\x00\xc1\x00\x00\x00\xc5\x00\x00\x00\xc7\x00\x00\x00\xd3\x00\x00\x00\xdf\x00\x00\x00\xe3\x00\x00\x00\xe5\x00\x00\x00\xe9\x00\x00\x00\xef\x00\x00\x00\xf1\x00\x00\x00\xfb\x00\x00\x00']`
And knowing the fact that these bytes will be casted to be int32 and every int32 is 4 bytes, also we know that the bytes are in little-endian format so a bytes array like `'\x03\x00\x00\x00'` is just 0x03 and so on</br>
So for now we have our key array to be 
```
[0x03,0x05,0x07,0x0b,0x0d,0x11,0x13,0x17,0x1D,0x1F,0x25,0x29,0x2B,0x2F,0x35,0x3B,0x3D,0x43,0x47,0x49,0x4F,0x53,0x59,0x61,0x65,0x67,0x6B,0x6D,0x71,0x7F,0x83,0x89,0x8B,0x95,0x97,0x9D,0x0A3,0xA7,0xAD,0xB3,0xB5,0xbf,0xc1,0xc5,0xc7,0xd3,0xdf,0xe3,0xe5,0xe9,0xef,0xf1,0xfb]
```

So for this encryption function we have the output which is `IQHR}nxio_vtvk_aapbijsr_vnxwbbmm{` and the key</br>
This is a kind of a rotation encryption function so I assumed that I will got the right flag if just passed the output as input again and so on to get the write flag</br>
Also I rewrited it in python so as we can decrypt our string</br>
I made this script</br>

```python
key = [0x03,0x05,0x07,0x0b,0x0d,0x11,0x13,0x17,0x1D,0x1F,0x25,0x29,0x2B,0x2F,0x35,0x3B,0x3D,0x43,0x47,0x49,0x4F,0x53,0x59,0x61,0x65,0x67,0x6B,0x6D,0x71,0x7F,0x83,0x89,0x8B,0x95,0x97,0x9D,0x0A3,0xA7,0xAD,0xB3,0xB5,0xbf,0xc1,0xc5,0xc7,0xd3,0xdf,0xe3,0xe5,0xe9,0xef,0xf1,0xfb]
def enc(inp):
    inp = list(inp)
    for i in range(len(inp)):
        current_char = ord(inp[i])
        v17 = ord(inp[i]) + key[i]
        if current_char > 96 and current_char <= 122:
            v6 = 122
        else:
            if (current_char > 96 and current_char <= 122 or current_char > 64 and current_char <= 90) and not (current_char > 96 and current_char <= 122):
                v6 = 90
            else:
                v6 = current_char
        while v17 > v6: v17 -= 26
        if current_char == 123:
            v12 = 125
        else:
            if current_char == 125:
                v12 = 123
            else:
                if current_char > 96 and current_char <= 122 or current_char > 64 and current_char <= 90:
                    v12 = v17
                else:
                    v12 = current_char
        inp[i] = chr(v12)
    return ''.join(inp)


flag="IQHR}nxio_vtvk_aapbijsr_vnxwbbmm{"
while True:
    if "FLAG" in flag:
        print(flag)
        break
    flag = enc(flag)
```

Run it to get the right flag</br>
# Flag
FLAG{well_keep_training_yourself}
