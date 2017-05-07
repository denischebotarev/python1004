def user_numbers():
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))
    counter = 1
    for dummy_row in range(row):
        for dummy_col in range(col):
            print(counter, end = ' ')
            counter += 1
        counter = counter - col + 1
        print()

user_numbers()
