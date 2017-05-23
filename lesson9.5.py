class A:
    def method(self):
        print('A')


class B(A):
    pass


class C:
    def method(self):
        print('C')


class D(B, C):
    pass


class E(C, B):
    pass

e = E()
e.method()

d = D()
d.method()