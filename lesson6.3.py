# def func(*args, **kwargs):
#     for arg in args:
#         print(arg)
#
#     for key in kwargs.keys():
#         print(kwargs[key])
#
#     return args, kwargs
#
# print(func(2, [77, 66], 4, a='abc', name='Tom', grades=[23,56,69]))

def func(*args):
    rez = 0
    for arg in args:
        rez += arg
    return rez

lst = list(range(1, 101))
print(func(*lst)) # func(1, 2, 3...99, 100)