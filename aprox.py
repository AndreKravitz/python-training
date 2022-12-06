target = int(input('Type a Natural number: '))
epsilon = 0.0001
next = epsilon**2
answer = 0.0

while abs(answer**2 - target) >= epsilon and answer <= target:
    print(abs(answer**2 - target), answer)
    answer += next

if abs(answer**2 - target) >= epsilon:
    print(f'Sorry. I could not find the square foot of {target}')
else:
    print(f'{target} is the square foot of {answer}')
