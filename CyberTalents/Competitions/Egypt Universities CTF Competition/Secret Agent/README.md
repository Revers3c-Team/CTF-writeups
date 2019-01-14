# Category
Web Security
# Level
Medium
# Points
100
# Description
```Only a true secret agent can see the flag, could you ?```
# Link
http://35.225.49.73/secretagent/
# Solution
With some invistigation we have two important things</br>
1) There's a cookie named `login` with value `False`</br>
2) The robots file at `/robots` contains</br>
```
User-agent: kiki
Allow: /VGgzUzNjcmV0UGF0aAo=
```
that allows requests to `/VGgzUzNjcmV0UGF0aAo=` for User-agent `kiki` only</br>
So we make a request to `/VGgzUzNjcmV0UGF0aAo=/` with `login` cookie set to `True` and User-agent to `kiki` using burp</br>

And this is how we get the flag</br>
