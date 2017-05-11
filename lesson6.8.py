x = 0

def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print('inner x=', x)

    inner()
    print('outer x =', x)

outer()
print('global x=', x)