file = open('word.txt')
word = list(file.read())
answ = []
for i in range(len(word)):
    answ.append('_')
out = ''
for i in answ:
    out += i + ' '
print(out)
incor = []
indt = 0
while indt <= 10:
    let = input('Enter letter: ')
    if not let.isalpha() or len(let) > 1:
        print('Incorrect letter: ')
    else:
        file = False
        for i in range(len(word)):
            if let == word[i]:
                file = True
                answ[i] = word[i]
        if file == False:
            if let not in incor:
                print('Incorrect (')
                incor.append(let)
                indt += 1
            else:
                print('You have already entered this letter, and it is incorrect ! ')
        else:
            print('Correct !')
        out = ''
        for i in answ:
            out += i + ' '
        print(out)
        if answ == word:
            print('You WON !')
            break
        out = ''
        for i in incor:
            out += i + ', '
        print('Incorrect letters: ' + out)
        if indt == 1:
            print('    \n    \n    \n   _')
        if indt == 2:
            print('    \n    \n    \n ___')
        if indt == 3:
            print('    \n    \n    \n|___')
        if indt == 4:
            print('    \n    \n|   \n|___')
        if indt == 5:
            print('    \n|   \n|   \n|___')
        if indt == 6:
            print(' _  \n|   \n|   \n|___')
        if indt == 7:
            print(' _ _\n|   \n|   \n|___')
        if indt == 8:
            print(' _ _\n|  o\n|   \n|___')
        if indt == 9:
            print(' _ _\n|  o\n| / \n|___')
        if indt == 10:
            print(' _ _\n|  o\n| /|\n|___')
            print('You lose (')
            break