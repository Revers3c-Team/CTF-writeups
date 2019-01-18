# Category
Malware Reverse Engineering
# Level
Easy
# Points
50
# Description
flag format flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx},only a-z,0-9,_ are allowed. try to find the only flag that makes sense. Note: no special hardware is required to bruteforce https://www.youtube.com/watch?v=hyk46UmJPS4 this may help you coding the solution. DON'T BRUTEFORCE KEY SUBMISSIONS.
# File
[bruteforceme.py](https://raw.githubusercontent.com/Revers3c-Team/CTF-writeups/master/CyberTalents/Competitions/Al-Azhar%20University%20Cybersecurity%20CTF%20Competition/Bruteforce%20Me/bruteforceme.py)
# Solution
We have this script

```python
ll =[51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55, 50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]

i = raw_input()
ss= 0 
try:
    for ii in range(0,46 , 2):
        temp = i[ii:ii+2]
        temp = int(temp,0x10)
        ss+=temp
        temp >>=1
        if temp != ll[ii/2]:
            print "Something is wrong"
    if ss !=2406:
            print ss/0
    print "This flag may or may not work, can you find more ?"
        
except:
    print "NO"
```

Which does this</br>
1) Defines the list `ll`, receives input of user into `i`, starts a loop in range of 0 to 46 with step 2, at every iteration `temp` equals a chunk of two chars from the input, and it will be decoded as hex to int, it will be added to `ss`</br>
2) After that it will be divided by 2 (right shifting by 1 bit), and a check is made to make sure `temp` equals an equivalent-index item from `ll` list</br>
3) After the loop ends it will make sure `ss` equals 2406, and this will be one of the solutions (may or may not be right)

So I made these assumptions
1) Our input length should be 46</br>
2) The input must be the hex-encoded flag so the right flag must be 23 chars</br>
3) First I thought it's very easy as we can just multiply `ll` list by 2 and it decode it as ascii and it will be the flag</br>
4) I was wrong because of the fact that the dividing operation here will return only the quotient (the remainder is lost)</br>
```python
>>> 55 >> 1 == 54 >> 1 == 27
True
```
5) For now we know that the flag is the ascii decoded list `[102, 108, 98, 102, 122, 114, 100, 108, 96, 104, 110, 100, 100, 114, 94, 104, 114, 94, 108, 48, 114, 116, 124]` (`ll` * 2) but every number may be itself or added to 1</br>
6) There are too many possibilities here (about 2^23 possible solution), we can brute force the flag if just figured out an algorithm for a recursive function that will generate all the possible lists</br>

So I made this script to brute force the flag</br>

```python
ll =[51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55, 50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]
ll = [i*2 for i in ll]
def get_instance(i=0,c_list=[0] * 23):
    if i == 23:
        if sum(c_list) == 2406:
            string = ''.join([chr(i) for i in c_list])
            if string.startswith('flag{') and string.endswith("}"):
                print(string)
        return
    c_list[i] = ll[i]
    get_instance(i+1,c_list)
    c_list[i] = ll[i] + 1
    get_instance(i+1,c_list)
get_instance()
```

The output was</br>

```
flag{rdl`hndes_is_m1su}
flag{rdl`hneds_is_m1su}
flag{rdl`hneer_is_m1su}
flag{rdl`hnees^is_m1su}
flag{rdl`hnees_hs_m1su}
flag{rdl`hnees_ir_m1su}
flag{rdl`hnees_is^m1su}
flag{rdl`hnees_is_l1su}
flag{rdl`hnees_is_m0su}
flag{rdl`hnees_is_m1ru}
flag{rdl`hnees_is_m1st}
flag{rdl`hodds_is_m1su}
flag{rdl`hoder_is_m1su}
flag{rdl`hodes^is_m1su}
flag{rdl`hodes_hs_m1su}
flag{rdl`hodes_ir_m1su}
.....
```

Based on the output I kept adding filters and testing it so the last one is </br>

```python
ll =[51, 54, 48, 51, 61, 57, 50, 54, 48, 52, 55, 50, 50, 57, 47, 52, 57, 47, 54, 24, 57, 58, 62]
ll = [i*2 for i in ll]
def get_instance(i=0,c_list=[0] * 23):
    if i == 23:
        if sum(c_list) == 2406:
            string = ''.join([chr(i) for i in c_list])
            if string.startswith('flag{') and string.endswith("}") and "_is_" in string and "`" not in string and ("l1st" in string or "m0st" in string or "l0st" in string):
                print(string)
        return
    c_list[i] = ll[i]
    get_instance(i+1,c_list)
    c_list[i] = ll[i] + 1
    get_instance(i+1,c_list)
get_instance()
```

Now the output reduced to be 182 possible solution, I redirected it to a file and opened it with vscode</br>
I've also installed this [plugin](https://marketplace.visualstudio.com/items?itemName=ban.spellright) in vscode to check the syntax</br>
And I got the flag</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Al-Azhar%20University%20Cybersecurity%20CTF%20Competition/Bruteforce%20Me/img1.PNG)

# Flag
flag{remainder_is_l0st}
