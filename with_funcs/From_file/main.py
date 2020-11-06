import random
from with_funcs.funcs import main


def rand_word() -> str:
    with open('words.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        while True:
            word = random.choice(lines)
            word = word.strip()
            yield word


if __name__ == '__main__':
    while True:
        status = main(next(rand_word()))
        if not status:
            break

