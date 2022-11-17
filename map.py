numbers = [1, 2, 3, 4]
numbers_times_two = []
# Long version of code
for i in numbers:
    numbers_times_two.append(i * 2)
# Short version of code with map function
numbers_times_three = list(map(lambda i: i * 3, numbers))

print(numbers)
print(numbers_times_two)
print(numbers_times_three)


numbers_1 = [10, 15, 20, 13]
numbers_2 = [10, 15, 30]

print(numbers_1)
print(numbers_2)
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
# result = 20, 30, 50, None(Because numbers_2 doesn't contain 4 numbers and is shorter than numbers_1)
print(result)
