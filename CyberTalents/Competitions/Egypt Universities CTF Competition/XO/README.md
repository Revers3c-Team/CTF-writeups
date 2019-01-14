# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
```i am dead in the code find me```
# Solution
The binary is a non-stripped x64 linux binary</br>
So we load it in IDA</br>
The pseudo-code for main is</br>
```c++
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // eax
  char v4; // al
  int v6; // [rsp+0h] [rbp-10h]
  int v7; // [rsp+4h] [rbp-Ch]
  char v8; // [rsp+Bh] [rbp-5h]
  unsigned int v9; // [rsp+Ch] [rbp-4h]

  v9 = 1;
  do
  {
    board();
    if ( v9 & 1 )
      v3 = 1;
    else
      v3 = 2;
    v9 = v3;
    printf("Player %d, enter a number:  ", v3);
    __isoc99_scanf("%d", &v6);
    if ( v9 == 1 )
      v4 = 88;
    else
      v4 = 79;
    v8 = v4;
    if ( v6 != 1 || byte_4059 != 49 )
    {
      if ( v6 != 2 || byte_405A != 50 )
      {
        if ( v6 != 3 || byte_405B != 51 )
        {
          if ( v6 != 4 || byte_405C != 52 )
          {
            if ( v6 != 5 || byte_405D != 53 )
            {
              if ( v6 != 6 || byte_405E != 54 )
              {
                if ( v6 != 7 || byte_405F != 55 )
                {
                  if ( v6 != 8 || byte_4060 != 56 )
                  {
                    if ( v6 != 9 || byte_4061 != 57 )
                    {
                      printf("Invalid move ", &v6);
                      --v9;
                      getch();
                    }
                    else
                    {
                      byte_4061 = v8;
                    }
                  }
                  else
                  {
                    byte_4060 = v8;
                  }
                }
                else
                {
                  byte_405F = v8;
                }
              }
              else
              {
                byte_405E = v8;
              }
            }
            else
            {
              byte_405D = v8;
            }
          }
          else
          {
            byte_405C = v8;
          }
        }
        else
        {
          byte_405B = v8;
        }
      }
      else
      {
        byte_405A = v8;
      }
    }
    else
    {
      byte_4059 = v8;
    }
    v7 = checkwin();
    ++v9;
  }
  while ( v7 == -1 );
  board();
  if ( v7 == 2 )
    mem();
  if ( v7 == 1 )
    printf("==>\aPlayer %d win ", --v9);
  else
    printf("==>\aGame draw", &v6);
  getch();
  return 0;
}
```
This is a kind of XO game and the flag is not related with it at all</br>
We first spot the different functions</br>
for function `board`</br>
```c++
int board()
{
  system("cls");
  puts("\n\n\tTic Tac Toe\n");
  puts("Player 1 (X)  -  Player 2 (O)\n\n");
  puts("     |     |     ");
  printf("  %c  |  %c  |  %c \n", byte_4059, byte_405A, byte_405B);
  puts("_____|_____|_____");
  puts("     |     |     ");
  printf("  %c  |  %c  |  %c \n", byte_405C, byte_405D, byte_405E);
  puts("_____|_____|_____");
  puts("     |     |     ");
  printf("  %c  |  %c  |  %c \n", byte_405F, byte_4060, byte_4061);
  return puts("     |     |     \n");
}
```
It is just a part of the game</br>
And the same thing for function `checkwin`</br>
For the function `mem` (will be executed at some condition)</br>
```c++
int mem()
{
  size_t v0; // rbx
  char v2[32]; // [rsp+0h] [rbp-90h]
  char v3; // [rsp+20h] [rbp-70h]
  char v4; // [rsp+21h] [rbp-6Fh]
  char v5; // [rsp+22h] [rbp-6Eh]
  char v6; // [rsp+23h] [rbp-6Dh]
  char v7; // [rsp+24h] [rbp-6Ch]
  char v8; // [rsp+25h] [rbp-6Bh]
  char v9; // [rsp+26h] [rbp-6Ah]
  char v10; // [rsp+27h] [rbp-69h]
  char v11; // [rsp+28h] [rbp-68h]
  char v12; // [rsp+29h] [rbp-67h]
  char v13; // [rsp+2Ah] [rbp-66h]
  char v14; // [rsp+2Bh] [rbp-65h]
  char v15; // [rsp+2Ch] [rbp-64h]
  char v16; // [rsp+2Dh] [rbp-63h]
  char v17; // [rsp+2Eh] [rbp-62h]
  char v18; // [rsp+2Fh] [rbp-61h]
  char v19; // [rsp+30h] [rbp-60h]
  char v20; // [rsp+31h] [rbp-5Fh]
  char v21; // [rsp+32h] [rbp-5Eh]
  char v22; // [rsp+33h] [rbp-5Dh]
  char v23; // [rsp+34h] [rbp-5Ch]
  char v24; // [rsp+35h] [rbp-5Bh]
  char v25; // [rsp+36h] [rbp-5Ah]
  char v26; // [rsp+37h] [rbp-59h]
  char v27; // [rsp+38h] [rbp-58h]
  char v28; // [rsp+39h] [rbp-57h]
  char v29; // [rsp+3Ah] [rbp-56h]
  char v30; // [rsp+3Bh] [rbp-55h]
  char v31; // [rsp+3Ch] [rbp-54h]
  char v32; // [rsp+3Dh] [rbp-53h]
  char v33; // [rsp+3Eh] [rbp-52h]
  char v34; // [rsp+3Fh] [rbp-51h]
  char v35; // [rsp+40h] [rbp-50h]
  char v36; // [rsp+41h] [rbp-4Fh]
  char s; // [rsp+50h] [rbp-40h]
  char v38; // [rsp+51h] [rbp-3Fh]
  char v39; // [rsp+52h] [rbp-3Eh]
  char v40; // [rsp+53h] [rbp-3Dh]
  char v41; // [rsp+54h] [rbp-3Ch]
  char v42; // [rsp+55h] [rbp-3Bh]
  char v43; // [rsp+56h] [rbp-3Ah]
  char v44; // [rsp+57h] [rbp-39h]
  char v45; // [rsp+58h] [rbp-38h]
  char v46; // [rsp+59h] [rbp-37h]
  char v47; // [rsp+5Ah] [rbp-36h]
  char v48; // [rsp+5Bh] [rbp-35h]
  char v49; // [rsp+5Ch] [rbp-34h]
  char v50; // [rsp+5Dh] [rbp-33h]
  char v51; // [rsp+5Eh] [rbp-32h]
  char v52; // [rsp+5Fh] [rbp-31h]
  char v53; // [rsp+60h] [rbp-30h]
  char v54; // [rsp+61h] [rbp-2Fh]
  char v55; // [rsp+62h] [rbp-2Eh]
  char v56; // [rsp+63h] [rbp-2Dh]
  char v57; // [rsp+64h] [rbp-2Ch]
  char v58; // [rsp+65h] [rbp-2Bh]
  char v59; // [rsp+66h] [rbp-2Ah]
  char v60; // [rsp+67h] [rbp-29h]
  char v61; // [rsp+68h] [rbp-28h]
  char v62; // [rsp+69h] [rbp-27h]
  char v63; // [rsp+6Ah] [rbp-26h]
  char v64; // [rsp+6Bh] [rbp-25h]
  char v65; // [rsp+6Ch] [rbp-24h]
  char v66; // [rsp+6Dh] [rbp-23h]
  char v67; // [rsp+6Eh] [rbp-22h]
  char v68; // [rsp+6Fh] [rbp-21h]
  char v69; // [rsp+70h] [rbp-20h]
  char v70; // [rsp+71h] [rbp-1Fh]
  char v71; // [rsp+7Bh] [rbp-15h]
  int i; // [rsp+7Ch] [rbp-14h]

  s = 49;
  v38 = 50;
  v39 = 51;
  v40 = 52;
  v41 = 53;
  v42 = 54;
  v43 = 55;
  v44 = 56;
  v45 = 57;
  v46 = 49;
  v47 = 50;
  v48 = 51;
  v49 = 52;
  v50 = 53;
  v51 = 54;
  v52 = 55;
  v53 = 56;
  v54 = 57;
  v55 = 49;
  v56 = 50;
  v57 = 51;
  v58 = 52;
  v59 = 53;
  v60 = 54;
  v61 = 55;
  v62 = 56;
  v63 = 57;
  v64 = 49;
  v65 = 50;
  v66 = 51;
  v67 = 52;
  v68 = 53;
  v69 = 54;
  v70 = 55;
  v3 = 119;
  v4 = 94;
  v5 = 82;
  v6 = 83;
  v7 = 78;
  v8 = 101;
  v9 = 67;
  v10 = 12;
  v11 = 109;
  v12 = 88;
  v13 = 113;
  v14 = 108;
  v15 = 0;
  v16 = 91;
  v17 = 2;
  v18 = 123;
  v19 = 97;
  v20 = 74;
  v21 = 120;
  v22 = 65;
  v23 = 108;
  v24 = 5;
  v25 = 70;
  v26 = 105;
  v27 = 6;
  v28 = 85;
  v29 = 73;
  v30 = 1;
  v31 = 64;
  v32 = 71;
  v33 = 0;
  v34 = 91;
  v35 = 66;
  v36 = 74;
  for ( i = 0; ; ++i )
  {
    v0 = i;
    if ( v0 >= 2 * strlen(&s) + 1 )
      break;
    v71 = *(&v3 + i) ^ *(&s + i);
    v2[i] = v71;
  }
  v2[i] = 0;
  return printf("%s \n", v2);
}
```
Which is unrelated with the game</br>
Here we have `&v3` a pointer to the array `{v3,v4,v5,v6,v7,v8,....}` one-char for each item</br>
And `&s` is a pointer to the array `{s,v38,v39,v40,v41,v42,....}` one char for each item</br>
Also we have `*(&v3 + i)` equals `&v3[i]` and `*(&s + i)` equals `&s[i]`</br>
And `strlen(&s)` will be 46 because the null terminator 0x00 will be at `v15`</br>
So the value `2 * strlen(&s) + 1` will be 93 that is a strange thing for the loop as the size of `v2` is just 32 so the process may crash at running this function</br>
After all we know that the loop will just xor the first array with the second one</br>
So with simple script we can get the result of that operation which is just the flag</br>

```python
>>> print(''.join(chr(i^ii) for i,ii in zip([49,50,51,52,53,54,55,56,57,49,50,51,52,53,54,55,56,57,49,50,51,52,53,54,55,56,57,49,50,51,52,53,54,55],[119,94,82,83,78,101,67,12,109,88,113,108,0,91,2,123,97,74,120,65,108,5,70,105,6,85,73,1,64,71,0,91,66,74])))
Flag{St4TiC_4n4LYsIs_1s_1mp0rt4nt}
```

# Flag
Flag{St4TiC_4n4LYsIs_1s_1mp0rt4nt}

