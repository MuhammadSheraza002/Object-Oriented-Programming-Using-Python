from pickle import *
from random import *
from Medicine import *
def main():
    medicines = []


def add_medicine(list):
    name=input('write name of medicine')
    list.append(medicine(name))

def update_quantity():
    sr_no = int(input('write sr no: '))
    if sr_no <= medicine.count:
        quantity = int(input('write new quantity: '))
        medicine.set_quantity(quantity)
        print('quantity updated successfully')

    else:
        print('write correct sr no')
def update_prices():
    sr_no = int(input('write sr no: '))
    if sr_no <= medicine.count:
        retail_price = int(input('write new quantity: '))
        medicine.set_retail_price(retail_price)
        medicine.set_sale_price()
        print('price updated successfully')

    else:
        print('write cotrrect sr no')


def print_medicine(list):
    sr_no = int(input('write sr no: '))
    HAS = True
    index = 1
    for i in list:
        if i.get_count==sr_no:
            print(str(i))
            HAS = False
            break
    if HAS:
        print('write right sr no: ')

def write_medicine_in_text_file(list):
    file = input('write name of file: ')
    f = open(file,'wb')
    sr_no = int(input('write sr no: '))
    HAS = True
    index = 1
    for i in list:
        if i.get_count == sr_no:
            dump(i,f)
            HAS = False
            break
    if HAS:
        print('write right sr no: ')

def write_medicine_in_text_file(list):
    file = input('write name of file: ')
    f = open(file,'rb')
    sr_no = int(input('write sr no: '))
    HAS = True
    index = 1
    for i in list:
        if i.get_count == sr_no:
            print(load(f))
            HAS = False
            break
    if HAS:
        print('write right sr no: ')










