import struct
import marks

def read_data(marks_list):
    file = open("result.csv", 'r')
    for line in file:
        r = line.rstrip().split(',')
	m =  marks.Marks(r[0],float(r[1]),float(r[2]),float(r[3]),int(r[4]),int(r[5]),int(r[6]))		
	marks_list.append(m)
    file.close()

def write_data(marks_list):
    file = open('result.bin', 'wb+')
    for mark in marks_list:
        binary_string = mark.get_rollno()+struct.pack('f',mark.get_q1()) +struct.pack('f',mark.get_q2())+struct.pack('f',mark.get_q3())+struct.pack('h',mark.get_pres())+struct.pack('h', mark.get_a1()) + struct.pack('h', mark.get_a2())
        file.write(binary_string)
    file.close()

def read_data_binary():
    file = open('result.bin', 'rb')
    data = file.read()
    for i in range(0, len(data), 28):
        line = data[i: i+28]
        m = marks.Marks(line[0:10], struct.unpack('f',line[10:14])[0], struct.unpack('f',line[14:18])[0], struct.unpack('f',line[18:22])[0], struct.unpack('h',line[22:24])[0], struct.unpack('h',line[24:26])[0], struct.unpack('h',line[26:28])[0])
        print (m)
    file.close()

#def calculate_print_statistics(marks_list):

    
def main():
    marks_list = []
    read_data(marks_list)
    for mark in marks_list:
        print(mark)
    marks.Marks.show_statistics()
    write_data(marks_list)
    #read_data_binary()
    
main()
