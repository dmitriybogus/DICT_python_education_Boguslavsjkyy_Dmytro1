import random
from string import ascii_lowercase

words = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(words)
set_randomword = set(random_word)
hide_word = "-" * len(random_word)
latterr = set()
wrong_lett = set()
tword = []
heals = 8
hight = len(random_word)

print("H A N G M A N")
print('')
while True:
    answer = input('Type "play" to play the game, "exit" to quit: ')
    print()
    if answer == "play":
        while heals != 0 and set_randomword != latterr:
            print()
            hide_word = ''
            for ch in random_word:
                if ch in latterr:
                    hide_word += ch
                else:
                    hide_word += "-"
            print(hide_word)

            lett = input("Input a letter: ")
            if len(lett) != 1:
                print('You should input a single letter')
            elif lett not in ascii_lowercase:
                print('Please enter a lowercase English letter')
            elif lett not in set_randomword:
                print("That letter doesn't appear in the word")
                heals -= 1
                wrong_lett.add(lett)
            else:
                latterr.add(lett)

        if set_randomword == latterr:
            print(f'You guessed the word {random_word}!')
            print('You survived!')
            print()
        else:
            print("You lost!")
            print()
    elif answer == 'exit':
        break
