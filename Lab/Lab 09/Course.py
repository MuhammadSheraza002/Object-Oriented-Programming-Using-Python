class Course:
    def __init__(self,code,title):
        self.__code = code
        self.__title = title

    def __str__(self):
        return f'Course code: {self.__code}\t Course title: {self.__title}'
