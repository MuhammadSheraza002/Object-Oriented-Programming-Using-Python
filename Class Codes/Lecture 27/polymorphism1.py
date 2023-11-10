class A:
    def f1(self):
        print('A F1')
    def f2(self):
        print('A F2')
class B:
    def f1(self):
        print('B F1')
    def f2(self):
        print('B F2')

def func(obj):
    obj.f1()
    obj.f2()


obj_A = A()
obj_B = B()
func(obj_A)
func(obj_B)
