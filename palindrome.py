def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    fliped_word = word[::-1]
    if word == fliped_word:
        return True
    else:
        return False


def run():
    word = input('Hey Pal, write a word: ')
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print('Palindrome!!!')
    else:
        print('Everything but Palindrome :(')


if __name__ == '__main__':
    run()
