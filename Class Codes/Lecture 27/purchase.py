class Purchase:

    def __init__(self, price='', taxes='', **kwargs):
        self.price = price
        self.taxes = taxes

    def __str__(self):
        s = 'PURCHASE DETAILS\n'
        s += 'selling price: {}'.format(self.price)
        s += '\nestimated taxes: {}'.format(self.taxes)
        return s

    def prompt_init():
        return dict(price=input("What is the selling price? "),
        taxes = input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)
