def user_numbers():
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))
    for row_count in range(1, row+1):
        for col_count in range(row_count, col+1):
            print(col_count, end=' ')
        col += 1
        print()

    # counter = 1
    # for dummy_row in range(row):
    #     for dummy_col in range(col):
    #         print(counter, end = ' ')
    #         counter += 1
    #     counter = counter - col + 1
    #     print()

user_numbers()
