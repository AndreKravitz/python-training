import random
def choose_options():
    options = ('rock', 'paper', 'sissor')
    user_option = input('rock, paper or sissors? => ')
    user_option = user_option.lower()
    if not user_option in options:
        print("That's not a valid option")
        # continue
        return None, None
    
    computer_option = random.choice(options)
    
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Draw!')
    elif user_option == 'rock':
        if computer_option == 'sissors':
            print('Rock smashes sissor!')
            print('User wins!')
            user_wins += 1
        else:
            print('Paper covers rock!')
            print('Program wins!')
            computer_wins += 1
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('Paper covers rock!')
            print('User wins!')
            user_wins += 1
        else:
            print('Sissor scratches paper!')
            print('Program wins!')
            computer_wins += 1
    elif user_option == 'sissors':
        if computer_option == 'paper':
            print('Sissor scratches paper!')
            print('User wins!')
            user_wins += 1
        else:
            print('Rock smashes sissor!')
            print('Program wins!')
            computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0 
    user_wins = 0
    rounds = 1 
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        rounds += 1
        
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        
        if computer_wins == 2:
            print('Program wins the game!')
            break
        if user_wins == 2:
            print('User wins the game!')
            break

run_game()        


# :<   <>   []