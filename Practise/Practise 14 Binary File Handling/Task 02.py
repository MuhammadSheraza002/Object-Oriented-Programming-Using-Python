import struct
import random as r
def write():
    list = [float(r.randint(-100000,100000)+r.random()) for i in range(100)]
    f = open('numbertask2.txt','w')
    for element in list:
        f.write(str(element)+' ')
    f.close()

    bf = open('binarynum.bin','wb')
    list_binary = [struct.pack('f',list[i]) for i in range(len(list))]
    for element in list_binary:
        bf.write(element)
    bf.close()

write()