class Stack:
    def __init__(self):
        self.data = []
        self.count = 0

    def push(self, element):
        self.data.append(element)
        self.count += 1

    def pop(self):
        if len(self.data) == 0:
            return -1
        self.count -= 1
        return self.data.pop(self.count)

    def see_top(self):
        if len(self.data) == 0:
            return -1
        return self.data[self.count-1]

def main():
    s = Stack()
    s.push(35)
    s.push(56)
    s.push(46)
    print (s.pop())
    print (s.pop())
    print (s.see_top())
    print (s.pop())
    print (s.pop())

main()

