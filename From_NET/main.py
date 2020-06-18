import requests
from funcs import main


def rand_word():
        resp = requests.get('https://random-word-api.herokuapp.com/word?number=1')
        word = resp.json()
        return word[0]


if __name__ == '__main__':
    while True:
        status = main(rand_word())
        if not status:
            break
