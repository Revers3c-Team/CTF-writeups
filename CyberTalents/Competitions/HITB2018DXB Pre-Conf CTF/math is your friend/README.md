# Category
Malware Reverse Engineering
# Level
Hard
# Points
200
# Description
Not Available
# File
[rev200](https://github.com/Revers3c-Team/CTF-writeups/blob/master/CyberTalents/Competitions/HITB2018DXB%20Pre-Conf%20CTF/math%20is%20your%20friend/rev200)
# Solution
The file is x64 non-stripped linux binary so let's load it to IDA</br>
I also used HexRays decompiler to get its c pseudo-code</br>
For the main function we have</br>

```c++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax
  int v4; // [rsp+1Ch] [rbp-4h]

  if ( argc > 1 )
  {
    v4 = check_password(argv[1], argv, envp);
    if ( v4 == -1 )
    {
      puts("Wrong password: at least look at disassembly");
      result = 2;
    }
    else if ( v4 == -2 )
    {
      puts("Wrong password: hint, it's a matrix");
      result = 3;
    }
    else
    {
      if ( !v4 )
      {
        puts("Congratulations!!!");
        print_password(argv[1]);
      }
      result = 0;
    }
  }
  else
  {
    printf("Usage: %s <password>\n", *argv, envp, argv);
    result = 1;
  }
  return result;
}
```

Which does this
1) Make sure you passed at least one argument to it</br>
2) Pass the first argument to `check_password`, and make some conditions based on the return</br>
3) Our target is `print_password` so the return should be 0</br>
4) We do not have to understand how print_password works, all we need to is to bypass `check_password`</br>

For `check_passeord` we have

```c++
signed __int64 __fastcall check_password(const char *a1)
{
  signed int i; // [rsp+10h] [rbp-30h]
  signed int j; // [rsp+14h] [rbp-2Ch]
  int v4; // [rsp+18h] [rbp-28h]
  signed int k; // [rsp+1Ch] [rbp-24h]
  char v6; // [rsp+20h] [rbp-20h]
  char v7; // [rsp+21h] [rbp-1Fh]
  char v8; // [rsp+22h] [rbp-1Eh]
  char v9; // [rsp+23h] [rbp-1Dh]
  char v10; // [rsp+24h] [rbp-1Ch]
  char v11; // [rsp+25h] [rbp-1Bh]
  char v12; // [rsp+26h] [rbp-1Ah]
  char v13; // [rsp+27h] [rbp-19h]
  char v14; // [rsp+28h] [rbp-18h]
  unsigned __int64 v15; // [rsp+38h] [rbp-8h]

  v15 = __readfsqword(0x28u);
  v6 = 79;
  v7 = 8;
  v8 = 29;
  v9 = 58;
  v10 = 81;
  v11 = 21;
  v12 = 49;
  v13 = 123;
  v14 = 114;
  if ( strlen(a1) != 9 )
    return 0xFFFFFFFFLL;
  for ( i = 0; i <= 2; ++i )
  {
    for ( j = 0; j <= 2; ++j )
    {
      v4 = 0;
      for ( k = 0; k <= 2; ++k )
        v4 = (a1[3 * k + j] * *(&v6 + 3 * i + k) + v4) % 127;
      if ( i == j )
      {
        if ( v4 != 1 )
          return 4294967294LL;
      }
      else if ( v4 )
      {
        return 4294967294LL;
      }
    }
  }
  return 0LL;
}
```

Which does this
1) We have this array `&v6 = {79,8,29,58,81,21,49,123,114}`</br>
2) Make sure length of `a1` (our input) is 9 if not returns 0xFFFFFFFF which is -1</br>
3) Start a loop and a nested loop with `i` and `j` in range 0 to 2</br>
4) Start another nested loop with `k` in range 0 to 2, assign `v4` to be 0, and make some operations on it</br>
5) We need to know that `*(&v6 + 3 * i + k) = &v6[k+3*i]`</br>
6) Make some conditions on `v4`</br>
7) If failed, it returns 4294967294 which is -2</br>

Now we know that `v4` should be 1 when `i == j` and should be 0 at `i != j`</br>

I made this script to solve it</br>

```python
v6 = [79,8,29,58,81,21,49,123,114]
equs = []
for i in range(3):
    for j in range(3):
        v4 = "0"
        if i == j: v4 = "1"
        equ = "0"
        for k in range(3):
            equ = "(a%d * %d + %s) %% 127" % (3 * k + j, v6[3 * i + k], equ)
        equ += " == " + v4
        equs.append(equ)

print("We need to solve these system of equations")
for equ in equs: print(equ)

print("We solve 3 equations with 3 variables (every variable in range of 33 -- 126) each time")
ii = 0
password = {}
for _ in range(3):
    check = []
    for equ in equs[ii::3]:
        check.append(equ)
    check = " and ".join(check)
    exec("""
for a{0} in range(33,127):
    for a{1} in range(33,127):
        for a{2} in range(33,127):
            if {3}:
                password[{0}] = a{0}
                password[{1}] = a{1}
                password[{2}] = a{2}
                break
    """.format(ii,3+ii,6+ii,check))
    ii += 1
print("The password is:"),
print("".join([chr(i) for i in [password.get(ii) for ii in list(set(password.keys()))]]))
print("Now run it again with ./rev200 \"<password>\"")
```

# Flag
flag{d1scr337_math_1s_gr3at}
