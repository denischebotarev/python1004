def symbols_in_stroka():
    stroka = input('Enter your phrase/word: ')
    symbol = input ('Enter your symbol: ')
    counter = 0
    for bukva in stroka:
        if bukva == symbol:
            counter += 1
    print(counter)

symbols_in_stroka()