 #Задача 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#************************
def compresultsion(txt):
    count = 1
    result = ""
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            result = result + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        result = result + str(count) + txt[-1]
    return result
#************************
def recovery(txt):
    num = ""
    result = ""
    for i in range(len(txt)):
        if txt[i].isdigit():
            num += txt[i]
        else:
            result += txt[i] * int(num)
            num = ""
    return result
#************************
def writingFile(txtf, flw):
    with open("d:/Мои документы/Алена/Обучение/8_5Python/Seminar5_#4/"+flw+".txt", "w") as fl:
        fl.write(txtf)
#************************
import os 
os.system('cls')

print("Программа реализует RLE алгоритм: модуль сжатия и восстановления данных.")
otvet = input("Желаете сами ввести текст или возьмем из файла?(да - сами, нет - из файла): ")
if otvet.lower() == "да" or otvet.lower() == "y":
    txt = input("Введите текст для сжатия: ")
else:
    with open("d:/Мои документы/Алена/Обучение/8_5Python/Seminar5_#4/file.txt", "r") as fl:
        txt = fl.read()

comTxt = compresultsion(txt)
writingFile(comTxt, "fileCom")
print(f"Сжатый текст: {comTxt},  записан в файл")

recTxt = recovery(comTxt)
writingFile(recTxt, "file")
print(f"Восстановленный текст: {recTxt}, записан в файл")