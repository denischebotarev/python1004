for num in range(2,10):
    if num % 3 == 0:
        print('Found a multiple of three number', num)
        continue
        print('After continue')
    print('just number', num)