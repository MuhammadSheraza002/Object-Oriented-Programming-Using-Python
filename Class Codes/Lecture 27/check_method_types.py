class Method_Types:
    class_var = 10
    def instance_method(self):
        print ('Instance Method')
    @classmethod
    def class_method(cls):
        cls.class_var += 1
        print (f'Class Method: {Method_Types.class_var}')
    @staticmethod
    def static_method():
        print (f'Static Method: {Method_Types.class_var}')

Method_Types.instance_method(Method_Types)
Method_Types.class_method()
Method_Types.static_method()

