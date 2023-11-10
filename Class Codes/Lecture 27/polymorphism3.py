class Batsman:
    def intro(self):
        print('Types of batsman')
    def play(self):
        print('Batsman play good')

class Opener(Batsman):
    def play(self):
        print('Opener face new ball')

class MiddleOrder(Batsman):
    def play(self):
        print('Middle Order face old ball')

class HardHitter(Batsman):
    def play(self):
        print('Hard Hitter hit boundaries')

obj_batsman = Batsman()
obj_openner = Opener()
obj_middle_order = MiddleOrder()
obj_hard_hitter = HardHitter()

obj_batsman.intro()
obj_batsman.play()

obj_openner.intro()
obj_openner.play()

obj_middle_order.intro()
obj_middle_order.play()

obj_hard_hitter.intro()
obj_hard_hitter.play()
