import struct
import copy

class BMP:
    def __init__(self, filename):
        file = open(filename,'rb')
        self.bm = file.read(2)
        self.skip1 = file.read(16)
        self.width = struct.unpack('i',file.read(4))[0]
        self.height = struct.unpack('i',file.read(4))[0]
        clrs_count = self.width * self.height * 3
        self.skip2 = file.read(28)
        self.clrs = file.read(self.width * self.height * 3)
        file.close()

    def write_image(self, filename):
        file = open(filename,'wb+')
        file.write(self.bm)
        file.write(self.skip1)
        file.write(struct.pack('i',self.width))
        file.write(struct.pack('i',self.height))
        file.write(self.skip2)
        file.write(self.clrs)
        file.close()

    def merge(self, image):
        #it is assumed that both images are of same dimension
        new_image = copy.deepcopy(self)
        clr_list = list(new_image.clrs)
        clrs_count = self.width*self.height*3
        for i in range(clrs_count):
           clr_list[i] = (self.clrs[i] + image.clrs[i]) // 2
        new_image.clrs = bytes(clr_list)
        return new_image


def main():
    image1 = BMP('f2.bmp')
    image2 = BMP('background.bmp')
    image3 = image1.merge(image2)
    image3.write_image('merge.bmp')
    print('Completed Successfully')


main()

