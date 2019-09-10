

from pwn import *
import struct








#bypass fibo sequence (nochk version)

## I will assume from here U R running the nochk server version i edited (to avoid writing code)

#f = ''
#f = f.join( ['\x00' if n == '' else n for n in y.split('\x00')[7:][-1::-1] ] )
#f = struct.unpack('>HH', f)


#bypass recv (norecv version)

#while ( not ( 'Well' in y ) ):
#    conn . send ('1') # send any byte

for i in range (256):
#remote ip
    p = process ('FibSocket_0_nochk_norecv.exe')
    sleep (0.5)
    conn = remote ('127.0.0.1',7777)
    sleep (1)
    y = conn.recv()

    print ( "received :" + y )
    sleep(1)
    conn . send ( struct . pack ('<I',i) )
    y = p.recv()
    print ( "Comand line :" + y )
    if ( ( 'Congrats' in y ) ):
        print ( "byte is :" + str(i) )
        break

