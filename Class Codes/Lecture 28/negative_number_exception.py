class NegativeNumberException(RuntimeError):
    def __init__(self, age):
        RuntimeError.__init__(self)
        self.age = age

    def __str__(self):
        return self.age
