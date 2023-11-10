import struct

def main():
    file = open('baloons.bmp','rb')
    bm = file.read(2)
    skip1 = file.read(16)
    width = struct.unpack('i',file.read(4))[0]
    height = struct.unpack('i',file.read(4))[0]
    clrs_count = width * height * 3
    skip2 = file.read(28)
    clrs = file.read(width * height * 3)
    file.close()
    clr_list = list(clrs)
    for i in range(0, clrs_count, 3):
        if clr_list[i] != clr_list[i+1] and clr_list[i] != clr_list[i+2]:
            clr_list[i] = 0
    clrs = bytes(clr_list)
    file = open('baloons_without_blue_with_background.bmp','wb+')
    file.write(bm)
    file.write(skip1)
    file.write(struct.pack('i',width))
    file.write(struct.pack('i',height))
    file.write(skip2)
    file.write(clrs)
    file.close()

main()
