import random

def select_park():
    slide = random.randint(0,1)
    swing = random.randint(0,1)
    monkey_bar = random.randint(0,1)
    if slide == 1:
        print ("Slide: yes", end = "  ")
    else:
        print ("Slide: no", end = "  ")
    if swing == 1:
        print ("Swing: yes", end = "  ")
    else:
        print ("Swing: no", end = "  ")
    if monkey_bar == 1:
        print ("Monkey_bar: yes")
    else:
        print ("Monkey_bar: no")
    YES = 1
    NO = 0
    print ("Here are your park choices:")
    if slide == NO and swing == NO and monkey_bar == NO:
        print ("\tNational Park")
    if swing == NO:
        print ("\tWonder Park")
    print ("\tLaser Park")
    if swing == NO and monkey_bar == NO:
        print ("\tFamily Park")
    print ("\tChildren Park")