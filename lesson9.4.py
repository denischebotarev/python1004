class Polite:
    def greeting(self):
        print('Hello!')


class Rude:
    def farewall(self):
        print('Go away!')


class MultiChild(Polite, Rude):
    pass

a = MultiChild()
a.greeting()
a.farewall()