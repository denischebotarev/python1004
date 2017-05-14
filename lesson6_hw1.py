def user_phrase():
    phrase = str(input('Enter phrase: '))
    return phrase

def shifr():
    secretnoe_slovo = ''

    for bukva in user_phrase():
        if bukva.isupper():
            secretnoe_slovo += bukva

    print(secretnoe_slovo)

shifr()