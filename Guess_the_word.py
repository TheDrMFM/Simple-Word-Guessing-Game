def just_to_hide():
    from time import sleep
    txt = 'Starting the game'
    print(txt, end='')
    for count in range(3):
        print('.', end='')
        sleep(0.5)
    for c in range(20):
        print()


def is_custom_word():
    print('Would you like to use a custom word? [Y/N]: ')
    while True:
        choice = str(input('>>> ')).upper().strip()
        if choice[0] == 'Y':
            return True
        elif choice[0] == 'N':
            return False
        else:
            print('Invalid Response. Type [Y/N]')


def get_random_word():
    from random import randint
    database = ['TEQUILA', 'PYTHON', 'LANGUAGE', 'ARRAY', 'CHEESE', 'FUNCTION', 'HYPOTETICAL', 'THEORY',
                'LUDACRIS', 'CREATURE']
    rd = randint(0, len(database) - 1)
    return database[rd]


def get_custom_word():
    print('Type your word')
    while True:
        word = str(input('>>> ')).upper()
        ans = str(input(f'Is {word} right? [Y/N] >>> ')).strip().upper()
        if ans == 'Y':
            return str(word)
        else:
            print('Retype your word')


def win(word, tries, errors):
    print(f"Congratulations, you've won! The word was {word}")
    print(f"You guessed it in {tries} tries, with {10 - errors} mistakes.")
    exit('The Game is Over')


def list_to_str(lst):
    txt = ''
    for e in lst:
        txt = txt + e
    return txt


def str_to_list(string):
    ls = []
    for e in string:
        ls.append(e)
    return ls


def hid(word):
    return '_' * len(word)


def game_engine(word):
    tries = 0
    errors = 10
    # Hidden word
    hidden = hid(word)
    # Check if there's enough tries
    while True:
        if hidden == word:
            win(word, tries, errors)
        if errors <= 0:
            exit(f"You're out of tries. The word was {word}")
    # If it does, this is the game loop:

        tries += 1
        print('Guess the word')
        for char in hidden:
            print(char, end=' ')
        print(f'({len(word)} letters)')
        print('Guess a Letter')
        while True:
            letter = str(input('>>> ')).upper()
            if letter == word:
                win(word, tries, errors)
            if len(letter) > 1 or len(letter) == 0:
                print('You shall type 1 (and only 1) letter')
            else:
                break

        finder = word.find(letter)
        if finder != -1:
            hidden = str_to_list(hidden)
            print(f'Congratulations. The word has {letter}')
            for char in range(len(word)):
                if word[char] == letter:
                    hidden[char] = letter
            hidden = list_to_str(hidden)

        else:
            errors -= 1
            print(f"The word doesn't have {letter}. You have {errors} tries left!")


def main():
    choice = is_custom_word()
    if choice:
        word = get_custom_word()
    if not choice:
        word = get_random_word()
    just_to_hide()
    game_engine(word)


if __name__ == '__main__':
    main()
