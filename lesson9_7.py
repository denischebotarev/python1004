class Wallet:
    def __init__(self, init_amount=0):
        self.init_amount = init_amount
        self.amount = self.init_amount

    def set_income(self, amount):
        self.amount += amount

    def set_expense(self, amount):
        self.amount -= amount

    def get_amount(self):
        return self.amount

if __name__ == '__main__':
    wallet = Wallet(300)
    print(wallet.get_amount())

    wallet.set_income(200)
    print(wallet.get_amount())

    wallet.set_expense(100)
    print(wallet.get_amount())