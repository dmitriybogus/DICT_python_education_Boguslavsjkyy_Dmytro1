
def doska():
    print('---------')
    print('| ' + coord[0], coord[1], coord[2] + ' | ')
    print('| ' + coord[3], coord[4], coord[5] + ' | ')
    print('| ' + coord[6], coord[7], coord[8] + ' |')
    print('---------')


coord = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
count = 1


def game():
    global count
    cc = input("Enter the coordinates:")
    while True:
        if count == 1 or count == 3 or count == 5 or count == 7:

            if cc == "1 1" and coord[0] == " ":
                coord[0] = "X"
                count += 1
                return doska()
            elif cc == "1 2" and coord[1] == " ":
                coord[1] = "X"
                count += 1
                return doska()
            elif cc == "1 3" and coord[2] == " ":
                coord[2] = "X"
                count += 1
                return doska()
            elif cc == "2 1" and coord[3] == " ":
                coord[3] = "X"
                count += 1
                return doska()
            elif cc == "2 2" and coord[4] == " ":
                coord[4] = "X"
                count += 1
                return doska()
            elif cc == "2 3" and coord[5] == " ":
                coord[5] = "X"
                count += 1
                return doska()
            elif cc == "3 1" and coord[6] == " ":
                coord[6] = "X"
                count += 1
                return doska()
            elif cc == "3 2" and coord[7] == " ":
                coord[7] = "X"
                count += 1
                return doska()
            elif cc == "3 3" and coord[8] == " ":
                coord[8] = "X"
                count += 1
                return doska()
            elif ("1 1" or "1 2" or "1 3" or "2 1" or "2 2" or "2 3" or "3 1" or "3 2" or "3 3") not in cc:
                print("You should enter numbers!")
                return game()
            else:
                print("This cell is occupied! Choose another one!")
                return game()
        else:
            if cc == "1 1" and coord[0] == " ":
                coord[0] = "O"
                count += 1
                return doska()
            elif cc == "1 2" and coord[1] == " ":
                coord[1] = "O"
                count += 1
                return doska()
            elif cc == "1 3" and coord[2] == " ":
                coord[2] = "O"
                count += 1
                return doska()
            elif cc == "2 1" and coord[3] == " ":
                coord[3] = "O"
                count += 1
                return doska()
            elif cc == "2 2" and coord[4] == " ":
                coord[4] = "O"
                count += 1
                return doska()
            elif cc == "2 3" and coord[5] == " ":
                coord[5] = "O"
                count += 1
                return doska()
            elif cc == "3 1" and coord[6] == " ":
                coord[6] = "O"
                count += 1
                return doska()
            elif cc == "3 2" and coord[7] == " ":
                coord[7] = "O"
                count += 1
                return doska()
            elif cc == "3 3" and coord[8] == " ":
                coord[8] = "O"
                count += 1
                return doska()
            elif ("1 1" or "1 2" or "1 3" or "2 1" or "2 2" or "2 3" or "3 1" or "3 2" or "3 3") not in cc:
                print("You should enter numbers!")
                return game()
            else:
                return game()


while True:
    if coord[0] == 'X' and coord[1] == 'X' and coord[2] == 'X':
        print('X wins')
        break
    elif coord[0] == 'O' and coord[1] == 'O' and coord[2] == 'O':
        print('O wins')
        break
    if coord[3] == 'X' and coord[4] == 'X' and coord[5] == 'X':
        print('X wins')
        break
    elif coord[3] == 'O' and coord[4] == 'O' and coord[5] == 'O':
        print('O wins')
        break
    if coord[6] == 'X' and coord[7] == 'X' and coord[8] == 'X':
        print('X wins')
        break
    elif coord[6] == 'O' and coord[7] == 'O' and coord[8] == 'O':
        print('O wins')
        break
    if coord[0] == 'X' and coord[3] == 'X' and coord[6] == 'X':
        print('X wins')
        break
    elif coord[0] == 'O' and coord[3] == 'O' and coord[6] == 'O':
        print('O wins')
        break
    if coord[1] == 'X' and coord[4] == 'X' and coord[7] == 'X':
        print('X wins')
        break
    elif coord[1] == 'O' and coord[4] == 'O' and coord[7] == 'O':
        print('O wins')
        break
    if coord[2] == 'X' and coord[5] == 'X' and coord[8] == 'X':
        print('X wins')
        break
    elif coord[2] == 'O' and coord[5] == 'O' and coord[8] == 'O':
        print('O wins')
        break
    if coord[0] == 'X' and coord[4] == 'X' and coord[8] == 'X':
        print('X wins')
        break
    elif coord[0] == 'O' and coord[4] == 'O' and coord[8] == 'O':
        print('O wins')
        break
    if coord[2] == 'X' and coord[4] == 'X' and coord[6] == 'X':
        print('X wins')
        break
    elif coord[2] == 'O' and coord[4] == 'O' and coord[6] == 'O':
        print('O wins')
        break
    if " " not in coord:
        print("Drew")
        break
    else:
        game()