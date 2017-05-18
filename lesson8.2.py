def my_power(x, n):
    if n == 0:
        return 1
    else:
        return x * my_power(x, n-1)

print(my_power(2, 4))

print(my_power(3, 7))