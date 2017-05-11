rez = map(lambda x: x ** 3, [2, 3, 4])

print(list(rez))

# почитать map() filter() reduce()

foo2 = lambda *args: args

print(foo2(1, 2, 3))

print((lambda x, y: x + y)('Py', 'thon'))