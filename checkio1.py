def checkio(*data):
    new_list = []
    for arg in data:
        if data.count(arg) >= 2:
            new_list.append(arg)
    return new_list


assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
