import random
import struct

def write():
    f = open('numbers.txt','w')
    list= [random.randint(-10000,10000) for i in range(100)]
    for i  in range(len(list)):
        f.write(str(list[i])+' ')

    f.close()

    fb = open('binarynumbers.bin','bw')
    binary_list = [struct.pack('i',list[i]) for i in range(len(list))]
    for i in range(len(list)):
        fb.write(binary_list[i])
    fb.close()

write()
