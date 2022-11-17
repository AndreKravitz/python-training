file = open('./text.txt')

'''
# Reads the file using .read and .readline
print(file.read()) # Reads all the lines
print(file.readline()) # Reads line 1
print(file.readline()) # Reads line 2
print(file.readline()) # Reads line 3
print(file.readline()) # Reads line ...
'''


# Reads the file, using for
for line in file:
    print(line)
file.close()  # Closes the file to avoid memory leaks

print('-' * 80)

# Reads the file using with and for / no need to close the file with file.close()
with open('./text.txt') as file:
    for line in file:
        print(line)
