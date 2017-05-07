def user_numbers():
    row = int(input('Enter row: '))
    col = int(input('Enter col: '))
    counter = 1
    for dummy_row in range(row):
        for dummy_col in range(col):
            print(counter, end = ' ')
            counter += 1
        print()


    # for num in range(0,number,row):
    #     for dummy_row in range(col):
    #         num +=1
    #         print(num, end=' ')
    #     print()



user_numbers()
