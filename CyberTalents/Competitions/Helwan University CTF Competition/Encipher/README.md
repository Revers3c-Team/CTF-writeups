# Category
Malware Reverse Engineering
# Level
Easy
# Points
50
# Description
Decrypt this string `0a0c073c5a55072c117e442b0c60501627614efd`
# File
[Encipher.exe](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Helwan%20University%20CTF%20Competition/Encipher/Encipher.exe)
# Solution
The file is x86 windows binary which will encrypt the input, so let's load it to IDA</br>
Our target function is `sub_4015C0` and it looks like this</br>

```c++
int sub_4015C0()
{
  FILE *File; // eax
  char *i; // eax
  signed int v3; // [esp+28h] [ebp-8h]
  signed int j; // [esp+2Ch] [ebp-4h]

  sub_401760();
  printf("[+] Enter text to encipher : ");
  File = off_403024(0);
  fgets(Buf, 22, File);
  v3 = strlen(Buf) - 1;
  for ( i = Buf; *i; ++i )
  {
    if ( i[1] == 10 )
    {
      *i ^= 0x80u;
      break;
    }
    *i ^= i[1];
  }
  printf("[+] Enciphered Text : ");
  for ( j = 0; j < v3; ++j )
    printf("%x%x", (Buf[j] >> 4), Buf[j] & 0xF);
  getch();
  return 0;
}
```

Which does this</br>
1) Reads from stdin a string limited to 22 chars, and stores its address to `Buf`</br>
2) It loops through the input chars (from the start to the first null byte) and at every iteration it will</br>
a) Check if the next char ascii code is 10 (if the next char is '\n') and if so it xor the current char with 0x80 and breaks</br>
b) Xor current char with the next char</br>
3) Prints the output in hex</br>

So basically all it's doing is xoring every char with the next one and at the last char it xor it with 0x80</br>
So to reverse this all we need to do is to xor the last char with 0x80 and make the same operation but in the inverse direction</br>
I made this script</br>

```python
>>> enc_flag = '0a0c073c5a55072c117e442b0c60501627614efd'.decode('hex')
>>> flag = ""
>>> ch = 0
>>> for i in range(len(enc_flag))[::-1]:
...   hex_ch = ord(enc_flag[i])
...   if i == len(enc_flag) - 1:
...    ch = hex_ch ^ 0x80
...   else:
...    ch = hex_ch ^ ch
...   flag += chr(ch)
...
>>> print(flag[::-1])
FL@G{!ts_N0t_S3cuR3}
```

# Flag
FL@G{!ts_N0t_S3cuR3}
