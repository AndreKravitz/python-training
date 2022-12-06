numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'F'
    print(output)

print('-' * 10)

# Only in Python …
for x in numbers:
    print('F' * x)
