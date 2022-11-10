# Long version of code
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)
    
print(numbers)

# # Short version of code with List comprehensions

numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)    



# # List comprehension with: if

num = []
for i in range(1, 11):
    if i % 2 == 0:
        num.append(i * 2)
print(num)

num_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(num_v2)
