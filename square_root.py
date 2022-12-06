target = int(input('Type a Natural number: '))
answer = 0

while answer**2 < target:
    print(answer)
    answer += 1

if answer**2 == target:
    print(f'{answer} is the square root of {target}')
else:
    print(f'{target} does not have a exact square root.')
