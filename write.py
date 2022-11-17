with open('./texs.txt', 'w+') as file:
    for line in file:
        print(line)
        # .write adds a new line
    file.write('First new line\n')
    file.write('Second new line\n')
    file.write('Third new line\n')

# r+ adds new lines to the file
# w+ adds new lines to the file but overwriting the original content
