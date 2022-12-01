 #Задача 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

#************************
def DeletText(newtxt):
    newtxt = list(filter(lambda x: 'абв' not in x, newtxt.split()))
    return " ".join(newtxt)

#************************
import os 
os.system('cls')

print("Программа удаляет из текста все слова, содержащие ""абв"".")
txt = input("Введите текст: ")

delTxt = DeletText(txt)

print(f"Новый текст: {delTxt}")