class AppleBag:
    product = 'apple'

    def __init__(self, init_amount):
        self.apple_amount = init_amount

    def purchase(self, amount):
        self.apple_amount += amount

    def sale(self, amount):
        self.apple_amount -= amount

    def get_amount(self):
        return self.apple_amount


if __name__ == '__main__':
    bag = AppleBag(100)
    assert bag.product == 'apple'
    assert bag.get_amount() == 100

    bag.sale(10)
    assert bag.get_amount() == 90

    bag.purchase(30)
    assert bag.get_amount() == 120