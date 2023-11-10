import item

def main():
    i1=item.Item("A1",30,5)
    i2=item.Item("A2",70,2)
    i3=item.Item("A3",30,6)
    i4=item.Item("A4",90,1)
    i1.show()
    i2.show()
    i3.show()
    i4.show()
    i1.set_quantity(7)
    print (f'I1 quantity: {i1.get_quantity()}')
    print(i1.compare(i2))
    print(i1.compare(i3))
    print(i1.compare(i4))

main()

