# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
Not Available
# File
[mathmaster](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/HITB2018DXB%20Pre-Conf%20CTF/Math%20Master/mathmaster
)
# Solution
The file is x64 non-stripped linux binary so let's load it to IDA</br>
I also used HexRays decompiler to get its c pseudo-code</br>
For the main function we have</br>

```c++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax

  if ( argc == 2 )
  {
    if ( strlen(argv[1]) == 11 )
    {
      if ( check(argv[1]) )
        printf("flag{%s}\n", argv[1], argv);
      else
        puts("Wrong");
      result = 0;
    }
    else
    {
      puts("Please check the input length.");
      result = -1;
    }
  }
  else
  {
    puts("Please check the input value.");
    result = -1;
  }
  return result;
}
```

Which does this</br>
1) Make sure you passed at least one argument to it</br>
2) Make sure the length of the first argument is 11</br>
3) If so it will pass it to check function and print it as the right flag in case of non-zero return</br>

For the function `check`</br>

```c++
_BOOL8 __fastcall check(char *a1)
{
  if ( (*a1 ^ 0x4D) != (a1[10] != 82) )
    return 0LL;
  if ( *a1 * a1[1] != 4004 )
    return 0LL;
  if ( a1[1] * a1[2] != 6032 )
    return 0LL;
  if ( a1[2] * a1[3] != 8352 )
    return 0LL;
  if ( a1[3] + a1[4] != 167 )
    return 0LL;
  if ( a1[4] + a1[5] != 172 )
    return 0LL;
  if ( a1[5] + a1[6] != 141 )
    return 0LL;
  if ( 102 * a1[6] + 32 * a1[7] - 13 * a1[8] != 8700 sympy)
    return 0LL;
  if ( *a1 * a1[7] * a1[1] != 460460 )
    return 0LL;
  if ( a1[2] * a1[8] * a1[3] != 968832 )
    return 0LL;
  if ( a1[4] * a1[9] * a1[5] == 373065 )
    return a1[2] * a1[10] + a1[7] == 9627;
  return 0LL;
}
```

The code here is quite simple except for some points</br>
1) `*a1` is just `a1[0]`</br>
2) We need to pass all the conditions without return 0 so all conditions have to be false (except the last one)</br>
3) For example the first condition, both sides have to equal, but `(a1[10] != 82)` returns 0 or 1 and `(*a1 ^ 0x4D)` may return a range of numbers including 0 and 1 so there's two possibilities here</br>
a) Both are 1 but in this case we cannot get a[10] because it will be indeterminate</br>
b) Both are 0 and in this case we can get `a[0]` and `a[10]`</br>

To solve this system of equations I used sage math</br>

```python
from sage.all import *

_ = var(' '.join([('a%d') % i for i in range(11)]))

s = solve([ 
        a10 == 82,
        a0 * a1 == 4004,
        a1 * a2 == 6032,
        a2 * a3 == 8352,
        a3 + a4 == 167,
        a4 + a5 == 172,
        a5 + a6 == 141,
        102 * a6 + 32 * a7 - 13 * a8 == 8700,
        a0 * a7 * a1 == 460460,
        a2 * a8 * a3 == 968832,
        a4 * a9 * a5 == 373065,
        a2 * a10 + a7 == 9627
      ],a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
      
flag = "flag{"
for i in s[0]:
  flag += chr(int(str(i).split('==')[1]))

flag += "}"

print(flag)
```

We can also solve it with z3</br>

```python
from z3 import *

a = [Int('a[%d]' %i) for i in range(0,11)]

s = Solver()
s.add(
      a[10] == 82,
      a[0] * a[1] == 4004,
      a[1] * a[2] == 6032,
      a[2] * a[3] == 8352,
      a[3] + a[4] == 167,
      a[4] + a[5] == 172,
      a[5] + a[6] == 141,
      102 * a[6] + 32 * a[7] - 13 * a[8] == 8700,
      a[0] * a[7] * a[1] == 460460,
      a[2] * a[8] * a[3] == 968832,
      a[4] * a[9] * a[5] == 373065,
      a[2] * a[10] + a[7] == 9627
      )

_ = s.check()

flag = "flag{"
for i in range(len(a)):
    flag += chr(int(str(s.model()[a[i]])))

flag += "}"

print(flag)
```

We can also use sympy</br>

```python
from sympy import *

for i in range(11): exec("a{0} = symbols('a{0}')".format(i))

s = solve([
        a10 -82,
        a0 * a1 - 4004,
        a1 * a2 - 6032,
        a2 * a3 - 8352,
        a3 + a4 - 167,
        a4 + a5 - 172,
        a5 + a6 - 141,
        102 * a6 + 32 * a7 - 13 * a8 - 8700,
        a0 * a7 * a1 - 460460,
        a2 * a8 * a3 - 968832,
        a4 * a9 * a5 - 373065,
        a2 * a10 + a7 - 9627
    ], [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10])

flag = "flag{"
for i in s[0]:
  flag += chr(int(i))

flag += "}"

print(flag)
```

# Flag
flag{M4tH_M@st3R}
