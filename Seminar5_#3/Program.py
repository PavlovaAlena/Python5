 #Задача 3. Создайте программу для игры в ""Крестики-нолики"".

def gameplay(border):
    count =0
    vic = False
    while not vic:
        if count > 0:
            os.system("cls")
        interface(border)
        if count % 2 == 0:
            select("X")
        else:
            select("O")
        count +=1
        if count > 4:
            win = checkWinnings(border)
            if win:
                os.system("cls")
                interface(border)
                print(f"Игра окончена победой {win}")
                vic = True
                break
            if count == 9:
                os.system("cls")
                interface(border)
                print("Боевая ничья!)")

#************************
def interface(border):
    print("Игра в крестики-нолики")
    print("-"*12)
    for i in range(3):
        print("|", border[0+i*3],"|", border[1+i*3], "|", border[2+i*3], "|")
        print("-"*12)

#************************
def select(XO):
    valid = False
    while not valid:
        player = input(f"Ход для {XO} - выберите ячейку: ")
        try:
            player =int(player)
        except:
            print("Необходимо выбрать цифрами с 1й по 9ю ячейку")
            continue
        if player >= 1 and player <= 9:
            if(str(border[player-1]) not in "XO"):
                border[player-1] = XO
                valid = True
            else:
                print("Ячейка уже занята!")
        else:
            print("Попробуйте сделать выбор еще раз")

#************************
def checkWinnings(border):
    victory = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in victory:
        if border[i[0]] == border[i[1]] == border[i[2]]:
            return border[i[0]]
    return False

#************************
import os 
os.system("cls")

border = list(range(1,10))
gameplay(border)