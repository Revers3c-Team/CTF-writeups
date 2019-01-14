# Category
Digital Forensics
# Level
Medium
# Points
100
# Description
```Sometimes you need to hide secrets deeeeeep. Flag format flag{XXXXXXXXXX}```
# File
[repeat.zip](https://github.com/Revers3c-Team/CTF-writeups/raw/master/CyberTalents/Competitions/Egypt%20Universities%20CTF%20Competition/Repeat%20after%20me/repeat.zip)
# Solution
Unzip it to get file `flag` which also is zipped file</br>
The file is compressed more than one time with as zip</br>
So we may use some script to automate the unzipping process</br>

Unzipping script
```python
import zipfile, os
while os.path.isfile('flag'):
  os.rename('flag','_flag_')
  zipfile.ZipFile('_flag_', 'r').extractall('.')
  os.remove('_flag_')
```

The result will be a text file flag.txt containing the flag</br>
# Flag
flag{Scrip7ing_is_s0_4w3som3}
