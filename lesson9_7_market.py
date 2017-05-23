from lesson9_7 import Wallet
from lesson9_7_bag import AppleBag
from lesson9_7_trader import Trader


class Market:
    def deal(self, buyer, seller, price, amount):
        if buyer.is_allowed() and seller.is_allowed():
            buyer.wallet.set_expense(price * amount)
            seller.wallet.set_income(price * amount)
            seller.bag.sale(amount)
            buyer.bag.purchase(amount)
        else:
            print('Deal is not allowed, Underage!!!')


wallet1 = Wallet(300)
bag1 = AppleBag(0)
person1 = Trader(wallet1, bag1, 'Tom', 'M', 1992)

person2 = Trader(Wallet(0), AppleBag(100), 'Jane', 'F', 1974)

market = Market()
market.deal(person1, person2, 10, 25)

print(person1.wallet.get_amount())
print(person1.bag.get_amount())
print(person2.wallet.get_amount())
print(person2.bag.get_amount())