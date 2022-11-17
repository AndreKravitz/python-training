# Iteration (1 - 10) using for
for i in range(1, 11):
    print(i)

print('-' * 50)

# Iteration (1 - 4) using iter / next
my_iter = iter(range(1, 4))
print(my_iter)
print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # ERROR: Stop Iteration (iter ran out of items to iterate)
