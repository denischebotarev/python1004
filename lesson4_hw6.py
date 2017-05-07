from random import randint

list = []

def cube():
    a = randint(1, 6)
    return a

def lucky():
    while True:
        b = cube()
        list.append(b)
        if b == 6:
            break
    print(list)

lucky()


