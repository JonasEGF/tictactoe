from os import system, name 

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else:
        _ = system('clear')
def mostrar():
    print(f'{negocio[0:3]}\n{negocio[3:6]}\n{negocio[6:9]}')

def jogar():
    coord = int(input('Choose one \n 0 | 1 | 2  \n 3 | 4 | 5\n 6 | 7 | 8'))
    esc = str(input('X or O?')).upper()
    if esc not in ['x','X','o','O']:
        play = 'n'
        return('EEROU')
    else:
        if coord in range(9):
            negocio[coord] = esc
        else:
            return('OPA OPA PAROU')
            play = 'n'
play = input('Do you want to play? y/n')
if play != 'y':
    print('ok')
else:
    negocio = []
    play == 'y'
    print('Tic Tac Toe')
    for i in range(9):
        negocio += " "
    while play == 'y':
        for item in range(9):
                clear()
                mostrar()
                jogar()
                diagonal1 = negocio[0]+negocio[4]+negocio[8]
                diagonal2 = negocio[2]+negocio[4]+negocio[6]
                vert1 = negocio[0]+negocio[1]+negocio[2]
                vert2 = negocio[3]+negocio[4]+negocio[5]
                vert3 = negocio[6]+negocio[7]+negocio[8]
                horiz = negocio[0]+negocio[3]+negocio[6]
                horiz2 = negocio[1]+negocio[4]+negocio[7]
                horiz3 = negocio[2]+negocio[5]+negocio[8]
                if 'XXX' in [diagonal1,diagonal2,vert1,vert2,vert3,horiz,horiz2,horiz3]:
                    clear()
                    mostrar()
                    print('XXX')
                    play = 'n'
                    break
                elif 'OOO' in [diagonal1,diagonal2,vert1,vert2,vert3,horiz,horiz2,horiz3]:
                    clear()
                    mostrar()
                    print('OOO')
                    play = 'n'
                    break
        print('Adeus')