class Static_Class_Instance:
    count = 10

    def instance_method(self):
        print ('Instance Method')

    @classmethod
    def class_method(cls):
        print (f'Class Method: {cls.count}')

    @staticmethod
    def static_method():
        print (f'Static Method')
obj = Static_Class_Instance()
obj.static_method()
obj.class_method()
'''Static_Class_Instance().instance_method()
Static_Class_Instance().class_method()
Static_Class_Instance().static_method()
'''