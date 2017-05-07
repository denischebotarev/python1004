def user_table():
    user_symbol = input('Enter symblol: ')
    col = int(input('Enter col number: '))
    row = int(input('Enter row number: '))
    for col_i in range(col):
        for row_i in range(row):
            print(user_symbol, end=' ')
        print()
user_table()