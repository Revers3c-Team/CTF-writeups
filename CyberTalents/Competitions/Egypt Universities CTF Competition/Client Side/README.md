# Category
Web Security
# Level
Easy
# Points
50
# Description
```Client side password check isn't secure, is it ? The password is your flag. Note: Flag format flag{XXXXXXXXXX}```
# Link
http://35.225.49.73/login/login.html
# Solution
It's a normal login portal that requires only a password<br/>
Viewing the source reveals that the verification is done on the client side with this function<br/>
```javascript
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 3;
    if (checkpass.substring(split*8, split*9) == 'd!}') {
      if (checkpass.substring(split*7, split*8) == '4dd') {
        if (checkpass.substring(split*6, split*7) == '$_b') {
          if (checkpass.substring(split*5, split*6) == '3_i') {
           if (checkpass.substring(split*4, split*5) == '$id') {
            if (checkpass.substring(split*3, split*4) == 'nt_') {
              if (checkpass.substring(split*2, split*3) == 'li3') {
                if (checkpass.substring(split, split*2) == 'g{C') {
                  if (checkpass.substring(0,split) == 'fla') {
                    alert("You got the flag!")
                    }
                  }
                }
              }
            }
          }
        }
      }
    }

    else {
      alert("Incorrect password");
    }
  }
```
It checks the chunks of the password</br>
So we can reassemble them to get the flag
# Flag
flag{Cli3nt_$id3_i$_b4ddd!}
