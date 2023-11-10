class Purchase:
    def __init__(self, price, taxes):
        self.price = price
        self.taxes = taxes
    def __str__(self):
        s = 'PURCHASE DETAILS\n'
        s += 'selling price: {}'.format(self.price)
        s += '\nestimated taxes: {}'.format(self.taxes)
        return s
