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

obj_a = A()
obj_b = B()
for obj in (obj_a, obj_b):
    obj.f1()
    obj.f2()
