import random


def password_generator():
    UPP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    LOW = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    CHAR = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
            '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    NUM = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = UPP + LOW + CHAR + NUM

    password = []

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)

    password = "".join(password)
    return password


def run():
    password = password_generator()
    print('New password: ' + password)


if __name__ == '__main__':
    run()
