import functools

numbers = [1, 2, 3, 4, 5]


def accumualtor(counter, item):
    print('Counter => ', counter)
    print('Item => ', item)
    return counter + item


result = functools.reduce(accumualtor, numbers)

print(result)
