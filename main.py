'''
text = 'Python training'
print('JS' in text)
print('Python' in text)
if 'Python' in text:
    print('Well done')
else:
    print('Ok')
'''


'''
print(len(text))
print(text.upper())
print(text.lower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith('P'))
print(text.endswith('P'))
print(text.replace('Python', 'JS'))
print(text.capitalize())
print(text.title())
print(text.isdigit())
print('345'.isdigit())
'''


'''
print(text[0])
print(text[3])
size = len(text)
print('size =>', size)
print(text[size - 1])
print(text[-1])
print(text[0:6])
print(text[11:14])
print(text[:10])
print(text[4:-1])
print(text[4:])
print(text[:])
print(text[10:15:1])
print(text[10:15:2])
print(text[::2])
'''


'''
# CRUD Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'hola')
print(numbers)

numbers.insert(3, 'change')
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + tasks
print(new_list)

index = new_list.index('todo 2')
new_list[index] = 'todo changed'
print(new_list)

new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1, 4, 6, 3]
numbers_a.sort()
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort()
'''


'''
numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print('0 =>', numbers[0])
print('-1 =>', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

# CRUD
# numbers.append(10)
print(numbers)
# numbers[1] = 'change'

print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
'''
