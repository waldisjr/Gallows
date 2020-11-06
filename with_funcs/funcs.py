import string

alphabet = string.ascii_lowercase
used_letters = []
game_number = 0


def print_level(level):
    levels = [
        '',
        '/|\\',
        ' | \n | \n | \n/|\\',
        '  ___ \n | \n | \n | \n/|\\',
        '  ___\n |   |\n |  \n |  \n | \n/|\\',
        '  ___\n |   |\n |   0\n |  \n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n |  / \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n |  / \\\n/|\\',
    ]
    if 0 <= level < 11:
        print(levels[level])
        return True
    raise TypeError("Incorrect level !")


def print_field(field):
    print('Word: ', ' '.join(field))


def create_word_field(word):
    field = []
    for _ in word:
        field.append('_')
    return field


def winning_or_loosing(field, game_number):
    if "_" not in field:
        return True
    elif game_number >= 10:
        return False


def make_move(field, used, word):
    while True:
        new_letter = input('Enter letter: ')
        new_letter = new_letter.lower()
        if len(new_letter) == 1 and new_letter in alphabet and new_letter not in used:
            if new_letter in word:
                for i in range(len(word)):
                    if word[i] == new_letter:
                        field[i] = new_letter
                used.append(new_letter)
                return [field, used, word, True]
            used_letters.append(new_letter)
            return [field, used, word, False]
        else:
            print('You entered wrong data, try one more time !')


def main(word):
    field_word = create_word_field(word)
    print('We remember word for you.\n')
    while True:
        print_field(field_word)
        print_level(game_number)
        print('Used letters: ', ' '.join(used_letters))
        field_word, used_letters, word, in_word = make_move(field_word, used_letters, word)

        if not in_word:
            game_number += 1

        is_win = winning_or_loosing(field_word, game_number)
        if is_win:
            print('You won !')
            print(word)
            break

        if not is_win:
            print('You lose (')
            pprint(game_number)
            print(word)
            break


if __name__ == '__main__':
    main('test')
