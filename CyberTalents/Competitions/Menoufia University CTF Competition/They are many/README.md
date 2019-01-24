# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
`We need some scripts to help us, can you do it ? format flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}`
# File
[They-are-many](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Menoufia%20University%20CTF%20Competition/They%20are%20many/They-are-many)
# Solution
The file x86 linux binary, with a simple main function</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Menoufia%20University%20CTF%20Competition/They%20are%20many/img1.PNG)

And a quite huge number of non-called functions</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Menoufia%20University%20CTF%20Competition/They%20are%20many/img2.PNG)

For every function we have a similar code</br>

```c++
nt zjwtckvcplspzceiztil()
{
  size_t v0; // ebx
  int v2; // [esp+1Ch] [ebp-3Ch]
  int v3; // [esp+20h] [ebp-38h]
  int v4; // [esp+24h] [ebp-34h]
  int v5; // [esp+28h] [ebp-30h]
  char s[4]; // [esp+2Ch] [ebp-2Ch]
  int v7; // [esp+30h] [ebp-28h]
  int v8; // [esp+34h] [ebp-24h]
  int v9; // [esp+38h] [ebp-20h]
  int v10; // [esp+3Ch] [ebp-1Ch]
  int v11; // [esp+40h] [ebp-18h]
  int v12; // [esp+44h] [ebp-14h]
  int v13; // [esp+48h] [ebp-10h]
  int i; // [esp+4Ch] [ebp-Ch]

  *s = -737951595;
  v7 = -602679916;
  v8 = -803815276;
  v9 = -904279934;
  v10 = -1039282299;
  v11 = -804859518;
  v12 = -1022310248;
  v13 = 1236127;
  v2 = 243;
  v3 = 186;
  v4 = 117;
  v5 = 165;
  for ( i = 0; ; ++i )
  {
    v0 = i;
    if ( v0 >= strlen(s) )
      break;
    s[i] ^= *(&v2 + 4 * (i % 4));
  }
  return printf("%s", s);
}
```

So we need to execute all of these functions individually</br>
And because the only function called from `main` is (dynamically linked) `puts` we can use gdb to change its address to the address of any other function to execute it</br>
From IDA I got that will be assigned to `puts` which is `0x8084010`</br>
Also to list all functions with its addresses I used `nm -C --defined-only They-are-many`</br>
And to change the addresses I used `gdb -q ./They-are-many -ex start -ex 'set *0x8084010 = <address>' -ex continue -ex quit`</br>
So I made this script

```python
>>> import subprocess
>>> addresses = subprocess.Popen(['nm' ,"-C" ,"--defined-only", "They-are-many"], stdout=subprocess.PIPE).communicate()[0]
>>> for address in addresses.splitlines():
...     if ' T ' in address:
...         address_n = '0x' + address.split(' T ')[0]
...         address_s = address.split(' T ')[1]
...         if len(address_s) != 20: continue
...         print("Executing %s ..." % address_s)
...         out = subprocess.Popen(['gdb' ,"-q" ,"./They-are-many" ,"-ex" ,"start" ,"-ex" ,"set *0x8084010 = %s" % address_n ,"-ex" ,"continue" ,"-ex" ,"quit"], stdout=subprocess.PIPE).communicate()[0]
...         if 'flag' in out:
...             print('flag{%s}' % out.split("{")[1].split("}")[0])
...             break
... 
Executing aaibprtesbuqmniuymta ...
Executing aaqbwemuqxupmcssyqcd ...
Executing abhtwqbgkarwxmacqarf ...
Executing abqvzfoxxdqdhmgfkwmn ...
Executing acxzoudorrydauedwlri ...
Executing aekjmvsmtvdghymasgew ...
Executing aemjzkcqeyydidijeqjp ...
Executing aepidrmoyubzsfbljgfu ...
Executing aertfkzadhfppcrvyfeu ...
Executing afkgfdzkpywulbunahqg ...
Executing afokhuzjcdprqjjyzusg ...
Executing afqnbfgqcxpuuyjzauly ...
Executing aftepyyiyvkymgtbbjxw ...
Executing agiirnwmbghszrhufxdp ...
Executing agkfkhnwfsduseucuebq ...
Executing aigjtafwrnhsrpgnvmqz ...
Executing aigponinibmpyhbnhnkn ...
....
....
Executing nevhrehlallqpkkbfezq ...
Executing newucmpxxtguhkjcmelk ...
Executing nfkrynltgiwafnmazybe ...
Executing nfwkxnszpmjdzligchnd ...
Executing ngvlkhsxuzwuqxcdovzs ...
Executing ngybenipskvmegfntcor ...
Executing nhihpofhqmosedxfmyqd ...
Executing nhrycgyjkfkzjkkcjggo ...
flag{@ut0m@t10n_1s_y0ur_fr1end}
>>>
```

# Flag
flag{@ut0m@t10n_1s_y0ur_fr1end}
