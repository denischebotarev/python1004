def func(x, y, z):
    return x + y + z

dct = {'x': 1, 'y': 2, 'z': 3}

print(func(**dct)) #func(x=1, y=2, z=3)