target = int(input('Type a Natural number: '))
epsilon = 0.001
bottom = 0.0
top = max(1.0, target)
answer = (top + bottom) / 2

while abs(answer**2 - target) >= epsilon:
    print(f'bottom={bottom}, top={top}, answer={answer}')
    if answer**2 < target:
        bottom = answer
    else:
        top = answer

    answer = (top + bottom) / 2

print(f'{answer} is the square foot of {target}')
