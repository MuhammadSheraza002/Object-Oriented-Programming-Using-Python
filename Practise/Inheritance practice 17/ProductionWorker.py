from Employee import Employee

class ProductionWorker(Employee):
    def __init__(self,name,number,integer):
        super().__init__()
        Employee.__init__(self)
        shift=''
        if integer ==1 :
            shift += 'Night'
        else:
            shift += 'Day'
        self.shift = shift

    def __str__(self):
        return Employee.__str__(self) + 'Shift' + self.shift


from random import randint
def main():
    Pw = ProductionWorker('Muhammad Sheraz',622222,randint(0,1))
    print(Pw)
    print(Pw.__str__)

main()