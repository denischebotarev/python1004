def create_iterator(n):
    for num in range(1, n+1):
        yield num*num

my_iterator = create_iterator(5)

for item in my_iterator:
    print(item, end=" ")