print('Tic Tac Toe')
line1 = [' ', ' ', ' ']
line2 = [' ', ' ', ' ']
line3 = [' ', ' ', ' ']

for item in range(9):
    coord = input('Choose one 0 | 1 | 2 | \n 3 | 4 | 5\n 6 | 7 | 8')
    esc = input('X or O?')
    if coord == '0':
        line1[0] = esc
    elif coord == '1':
        line1[1] = esc
    elif coord == '2':
        line1[2] = esc
    elif coord == '3':
        line2[0] = esc
    elif coord == '4':
        line2[1] = esc
    elif coord == '5':
        line2[2] = esc
    elif coord == '6':
        line3[0] = esc
    elif coord == '7':
        line3[1] = esc
    elif coord == '8':
        line3[2] = esc
    else:
        print('Invalid Value')
        break
    diagonal1 = ''.join(line1[0] + line2[1] + line3[2])
    diagonal2 = ''.join(line1[2] + line2[1] + line3[0])
    vert1 = ''.join(line1[0] + line2[0] + line3[0])
    vert2 = ''.join(line1[1] + line2[1] + line3[1])
    vert3 = ''.join(line1[2] + line2[2] + line3[2])
    print(f"{line1}\n{line2}\n{line3}")
    if 'XXX' in ''.join(line1) or 'XXX' in ''.join(line2) or 'XXX' in ''.join(line3):
        print('XXX')
        break
    elif 'XXX' in diagonal1 or 'XXX' in diagonal2:
        print('X  X\n X\nX X')
        break
    elif 'XXX' in vert1 or 'XXX' in vert2 or 'XXX' in vert3:
        print('XXX')
        break
    elif 'OOO' in ''.join(line1) or 'OOO' in ''.join(line2) or 'OOO' in ''.join(line3):
        print('OOO')
        break
    elif 'OOO' in diagonal1 or 'OOO' in diagonal2:
        print('O  O\n X\nO O')
        break
    elif 'OOO' in vert1 or 'OOO' in vert2 or 'OOO' in vert3:
        print('OOO')
        break

