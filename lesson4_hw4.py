list = []

def list_element():
    while True:
        element = input('Your element (print \'exit\' to quit): ')
        if element == 'exit':
            break
        list.append(element)
    print(list)


list_element()
