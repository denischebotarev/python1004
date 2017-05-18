def my_factorial(n):
    if n == 0:
        return 1
    else:
        return my_factorial(n-1) * n

print(my_factorial(6))

def factorial(n):
    fact = 1
    counter = 1
    while counter <= n:
        fact *= counter
        counter += 1
    print(fact)

factorial(5)