#Задача 2. Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит 121 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
#За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом"".

from random import randint

def select(player, sweets, quantity):
    valid = False
    while not valid:
        move = input(f"Ход {player}. Сколько конфет берете? ")
        try:
            move = int(move)
            if move > 0 and move <= quantity and move <= sweets:
                sweets -= move
                valid = True
                print(f"Осталось {sweets} конфет, после того, как {player} забрал(а) {move} шт")
            else:
                print(f"Количество конфет, которые можно взять, должно быть в интервале от 1 до {quantity}, но не больше оставшегося количества - {sweets} шт")
        except:
            print("Конфеты д.б. целыми, а не надкусанными")
    return sweets

#************************
def select_bot(sweets, quantity):
    move = randint(1, quantity) if sweets >= quantity else randint(1, sweets)
    sweets -= move
    print("Ход бота")
    print(f"Осталось {sweets} конфет, после того, как бот забрал {move} шт")
    return sweets

#************************
def select_Intelbot(sweets, quantity):
    move = sweets % (quantity + 1)
    if move == 0:
        move = randint(1, quantity) if sweets >= quantity else sweets
    sweets -= move
    print("Ход умного бота")
    print(f"Осталось {sweets} конфет, после того, как умный бот забрал {move} шт")
    return sweets

#************************
def checkWinnings(sweets, choosMove, first_name, second_name):
    if sweets == 0:
        return first_name if choosMove % 2 == 0 else second_name
    else:
        return False

#************************
def player_bot ():
    player = input("Введите свое имя: ").upper()
    sweets = 121
    quantity = 28
    countWin = sweets // quantity
    choosMove = randint(0, 1)
    win = False
    while not win:
        if choosMove % 2 == 0:
            sweets = select(player, sweets, quantity)
        else:
            sweets = select_bot(sweets, quantity)
        if choosMove >= countWin - 1:
            temp = checkWinnings(sweets, choosMove, player, "Бот")
            if temp:
                print(f"{temp} выиграл(а)")
                win = True
        choosMove += 1

#************************
def player_Intelbot ():
    player = input("Введите свое имя: ").upper()
    sweets = 121
    quantity = 28
    countWin = sweets // quantity
    choosMove = randint(0, 1)
    win = False
    while not win:
        if choosMove % 2 == 0:
            sweets = select(player, sweets, quantity)
        else:
            sweets = select_Intelbot(sweets, quantity)
        if choosMove >= countWin - 1:
            temp = checkWinnings(sweets, choosMove, player, "Бот")
            if temp:
                print(f"{temp} выиграл")
                win = True
        choosMove += 1

#************************
def player_player ():
    firstPlayer = input("Введите имя первого игрока: ").upper()
    secondPlayer = input("Введите имя второго игрока: ").upper()
    sweets = 121
    quantity = 28
    countWin = sweets // quantity
    choosMove = randint(0, 1)
    win = False
    while not win:
        if choosMove % 2 == 0:
            sweets = select(firstPlayer, sweets, quantity)
        else:
            sweets = select(secondPlayer, sweets, quantity)
        if choosMove >= countWin - 1:
            temp = checkWinnings(sweets, choosMove, firstPlayer, secondPlayer)
            if temp:
                print(f"{temp} выиграл(а)")
                win = True
        choosMove += 1

#************************
import os 
os.system("cls")
print("Игра на дележ конфет: человек против человека или человек против бота.")
print("По условию игры на столе лежит 121 конфета. Игроки делают ход друг за другом. Первый ход определяется жеребьёвкой.")
print("За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.")
print("")

Game = input("Вы хотите играть с человеком или ботом? (1-человек, иное-бот): ")
if (Game == "1"):
    player_player()
else:
    intel = input("Вы выбрали игру с ботом. А с каким ботом хотите играть - умным или простым? (0-умный, иное - как повезет): ")
    if intel == "0":
        player_Intelbot()
    else:
        player_bot()