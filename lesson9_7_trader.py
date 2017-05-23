from datetime import datetime
from lesson9_7 import Wallet
from lesson9_7_bag import AppleBag


class Person:
    def __init__(self, name, gender, birth_year):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year

    @staticmethod
    def _get_current_year():
        return datetime.now().year

    def get_age(self):
        return self._get_current_year() - self.birth_year

    def is_allowed(self):
        return self.get_age() >= 18

class Trader(Person):
    def __init__(self, wallet, bag, name, gender, birth_year):
        self.wallet = wallet
        self.bag = bag
        super().__init__(name, gender, birth_year)

if __name__ == '__main__':
    wallet = Wallet(300)
    bag = AppleBag(100)
    trader = Trader(wallet, bag, 'Tom', 'M', 1992)

    assert trader.bag.get_amount() == 100