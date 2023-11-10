def ten_note(rupee):
    if rupee !=0:
        print(f"{int(rupee)} ten rupee note")
def fifty_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} fifty rupee note")
def one_hundred_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} one hundred rupee note")
def five_hundred_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} five hundred rupee note")
def one_thousand_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} thousand rupee note")
def five_thousand_note(rupee):
    if rupee != 0:
        print(f"{int(rupee)} five thousand rupee note")
def less_than_100(amount):
    if amount >= 50:
        fifty_note(1)
        if amount > 50:
            ten_note((amount - 50) // 10)
    elif amount < 50:
        ten_note(amount // 10)
def less_than_500(amount):
    if amount % 100==0:
        one_hundred_note(amount//100)
    elif amount > 100:
        one_hundred_note(amount // 100)
        less_than_100(amount)
    else:
        less_than_100(amount)
def less_than_1000:
    if amount > 500:
        if amount < 600:
            less_than_100(amount%100)
        elif amount > 600:
            five_hundred_note(1)
            






