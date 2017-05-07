list = []

def spisok():
    spiskov = int(input('Vvedite kolichestvo spiskov: '))
    elementov = int(input('Vvedite kolichestvo elementov: '))
    a = 1
    b = elementov + 1
    for dummy_i in range(spiskov):
        temp_list = []
        for n in range(a, b):
            temp_list.append(n)
        list.append(temp_list)
        a += 1
        b += 1
    print(list)

spisok()