import random
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3

print('''
      Guess my number and you'll win.
      Its between 1 and 10...
      ''')

while guess_count < guess_limit:
    guess = int(input('??? Guess... '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break
else:
    print('Sorry, you lost.')
