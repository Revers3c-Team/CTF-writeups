#from z3 import *

regA = 0
regB = 0
regC = 0
regD = 0

#bytes = bytearray ( open("target","rb").read() )
bytes = bytearray ( open("scratch","rb").read() )

#--- test bytes
#bytes = [0x10,0x30,0x00,0x78,0x10,0x00,0x00,0xFF]
input = "0123456789012345678901234567"

j = 0
i = 0
while( i < len(bytes) ):
#    print ("index : " + str(i) )
    t = bytes[i] >> 4
    r = bytes[i]        & 0b11
    ra= (bytes[i] >> 2) & 0b11
    if (t == 0xF):
        if (regA == 0):
            print ( chr(  ( 65536 - regD ) % 256 ) )
            regD = 0
            print (" syscall getchar()" )
            if ( j >= len(input) ):
                print ("Error : no input!") 
            print(" sent char :" + input[j] + " index : " + str (j))
            j = j + 1
        elif (regA == 1):
            print (" syscall putchar()")
            print (" text char printed : " + chr(regB % 256) )
        elif (regA == 2):
            print (" syscall exit() "   )
            break
        else:
            print ("ERROR: undefined behaviour!")
    elif (t == 1):
        value = bytes[i+1] | (bytes[i+2] << 8)

        if (r == 0):
            print ("mov regA," + str (value))
            regA = value
        if (r == 1):
            print ("mov regB," + str (value))
            regB = value
        if (r == 2):
            print ("mov regC," + str (value))
            regC = value
        if (r == 3):
            print ("mov regD," + str (value))
            regD = value
        i = i + 2
    elif (t == 2):

        if (r == 0):
            if (ra == 0):
                print ("mov regA,regA")
                regA = regA + regA
            if (ra == 1):
                print ("mov regA,regB")
                regA = regA + regB
            if (ra == 2):
                print ("mov regA,regC")
                regA = regA + regC
            if (ra == 3):
                print ("mov regA,regD")
                regA = regA + regD
        if (r == 1):
            if (ra == 0):
                print ("mov regB,regA")
                regB = regB + regA
            if (ra == 1):
                print ("mov regB,regB")
                regB = regB + regB
            if (ra == 2):
                print ("mov regB,regC")
                regB = regB + regC
            if (ra == 3):
                print ("mov regB,regD")
                regB = regB + regD
        if (r == 2):
            if (ra == 0):
                print ("mov regC,regA")
                regC = regC + regA
            if (ra == 1):
                print ("mov regC,regB")
                regC = regC + regB
            if (ra == 2):
                print ("mov regC,regC")
                regC = regC + regC
            if (ra == 3):
                print ("mov regC,regD")
                regC = regC + regD
        if (r == 3):
            if (ra == 0):
                print ("mov regD,regA")
                regD = regD + regA
            if (ra == 1):
                print ("mov regD,regB")
                regD = regD + regB
            if (ra == 2):
                print ("mov regD,regC")
                regD = regD + regC
            if (ra == 3):
                print ("mov regD,regD")
                regD = regD + regD
    elif (t == 3):
        value = bytes[i+1] | (bytes[i+2] << 8)

        if (r == 0):
            print ("add regA," + str (value))
            regA = regA + value
        if (r == 1):
            print ("add regB," + str (value))
            regB = regB + value
        if (r == 2):
            print ("add regC," + str (value))
            regC = regC + value
        if (r == 3):
            print ("add regD," + str (value))
            regD = regD + value
        i = i + 2
    elif (t == 4):
        if (r == 0):
            print ("not regA")
            regA = regA ^ 0b11111111
        if (r == 1):
            print ("not regB")
            regB = regB ^ 0b11111111
        if (r == 2):
            print ("not regC")
            regC = regC ^ 0b11111111
        if (r == 3):
            print ("not regD")
            regD = regD ^ 0b11111111
    elif (t == 5):
        value = bytes[i+1] | (bytes[i+2] << 8)

        if (r == 0):
            print ("mul regA," + str (value))
            regA = regA * value
        if (r == 1):
            print ("mul regB," + str (value))
            regB = regB * value
        if (r == 2):
            print ("mul regC," + str (value))
            regC = regC * value
        if (r == 3):
            print ("mul regD," + str (value))
            regD = regD * value
        i = i + 2
    elif (t == 6):
        print ("janz regB")
        if (regA != 0):
            i = regB - 1
            print ("regB = " + str(regB) )
            print ("Jump was TAKEN!")
        else:
            print ("Jump was NOT taken!")
    elif (t == 7):

        if (r == 0):
            if (ra == 0):
                print ("add regA,regA")
                regA = regA + regA
            if (ra == 1):
                print ("add regA,regB")
                regA = regA + regB
            if (ra == 2):
                print ("add regA,regC")
                regA = regA + regC
            if (ra == 3):
                print ("add regA,regD")
                regA = regA + regD
        if (r == 1):
            if (ra == 0):
                print ("add regB,regA")
                regB = regB + regA
            if (ra == 1):
                print ("add regB,regB")
                regB = regB + regB
            if (ra == 2):
                print ("add regB,regC")
                regB = regB + regC
            if (ra == 3):
                print ("add regB,regD")
                regB = regB + regD
        if (r == 2):
            if (ra == 0):
                print ("add regC,regA")
                regC = regC + regA
            if (ra == 1):
                print ("add regC,regB")
                regC = regC + regB
            if (ra == 2):
                print ("add regC,regC")
                regC = regC + regC
            if (ra == 3):
                print ("add regC,regD")
                regC = regC + regD
        if (r == 3):
            if (ra == 0):
                print ("add regD,regA")
                regD = regD + regA
            if (ra == 1):
                print ("add regD,regB")
                regD = regD + regB
            if (ra == 2):
                print ("add regD,regC")
                regD = regD + regC
            if (ra == 3):
                print ("add regD,regD")
                regD = regD + regD
    else:
        print("ERROR: unknown instruction")
        break
    i = i + 1
