def func(*args):
    for arg in args:
        print(arg)
    return args

# print(func(1, 2, 3, 4, 5, 'abc', [44, 55]))

def func2(*args):
    args = args[-1]
    return args

# print(func2(1, 2, 3, 4, 5))

def func3(*args):
    rez = 0
    for arg in args:
        rez += arg
    return rez

# print(func3(1, 2, 3, 4, 5))

def func4(**kwargs):
    return kwargs.keys()

print(func4(y=4, z=5, x=1))