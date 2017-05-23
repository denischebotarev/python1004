class Sample:
    def _privat(self):
        print("I'm privat")

    def __superprivate(self):
        print("I'm super privat")

a = Sample()
a._privat()
# a.__superprivate()
a._Sample__superprivate()