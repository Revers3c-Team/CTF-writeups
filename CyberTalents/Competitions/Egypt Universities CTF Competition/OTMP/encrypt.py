import sys

pt = sys.argv[1]
key = sys.argv[2]

s = list(pt)
for j in xrange(len(key)):
    key = key[1:] + key[:1]
    for i in xrange(len(s)):
        s[i] = chr(ord(s[i]) ^ ord(key[i % len(key)]))

open("flag.enc", "w").write("".join(s))
