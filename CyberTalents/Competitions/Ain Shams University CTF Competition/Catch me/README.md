# Category
Malware Reverse Engineering
# Level
Medium
# Points
100
# Description
`Catch me if you can`
# File
[CatchMe.exe](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Ain%20Shams%20University%20CTF%20Competition/Catch%20me/CatchMe.exe)
# Solution
The file is x86 window binary, so loaded it to IDA</br>
At the main function, there's nothing interesting

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Ain%20Shams%20University%20CTF%20Competition/Catch%20me/img1.PNG)

After some thinking, I decided to view the exported functions (View-->Open subviews-->Exports), I found `start` which leads to the main function and `TlsCallback_0` so I followed it</br>

![untitled](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Ain%20Shams%20University%20CTF%20Competition/Catch%20me/img2.PNG)

I also searched for it</br>
`TLS (thread local storage) calls are subroutines that are executed before the entry point .`</br>
So a malware author may use it to execute some code even before the entry point</br>
Here we have an anti-debugging method with `IsDebuggerPresent` api call</br>
If run normally, it will check if the file name itself is `i_got_it` (without extension)</br>
So I just changed its name to `i_got_it.exe` and executed it</br>

# Flag
flag{TLS_1S_G00D:)}
