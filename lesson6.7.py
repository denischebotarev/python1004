x = 1
y = 1
z = 1

def outer():
    y = 10
    z = 10
    def inner():
        z = 100
        print('x in inner', x)
        print('y in inner', y)
        print('z in inner', z)

    inner()

outer()