# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

# text = 'абвгдейка - это передача'
# string = 'абв'

# new_text = text.split()
# text_1 =' '.join(filter(lambda x: string not in x, new_text))
# print(f'Initial text => {text}\n string => {string}\n New text => {text_1}')





# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# def input_number():
#     '''
#     Функция принимает от пользователя начальное число конфет.
#     Производит проверку на корректность ввода.
#     '''
#     while True:
#         try:
#             num_cand = int(input('Сколько всего конфет?: '))
#             if num_cand > 0:
#                 break
#             else:
#                 print('Вы ввели не корректное значение!')
#         except ValueError:
#             print('Вы ввели не число!')
#     return num_cand  
   
# def input_max(num_cand): 
#     '''
#     Функция принимает от пользователя максимальное число конфет, которое может взять игрок. 
#     Производит проверку на корректность ввода.
#     '''
#     while True:
#             try:
#                 max_cand = int(input('Максимальное количество конфет, которое можно взять : '))
#                 if num_cand > max_cand > 1:
#                     break
#                 else:
#                     print('Вы ввели не корректное значение!')
#             except ValueError:
#                 print('Вы ввели не число!')
#     return max_cand              

# def input_min(max_cand): 
#     '''
#     Функция принимает от пользователя минимальное число конфет, которое может взять игрок. 
#     Производит проверку на корректность ввода.
#     '''
#     while True:
#             try:
#                 min_cand = int(input('Минимальное количество конфет, которое можно взять: '))
#                 if max_cand > min_cand > 0:
#                     break
#                 else:
#                     print('Вы ввели не корректное значение!')
#             except ValueError:
#                 print('Вы ввели не число!')
#     return min_cand              

# def input_num(min_cand, max_cand, num_cand, Player):
#     '''
#     Функция принимает от игрока  число конфет, которое он берет. 
#     Производит проверку на корректность ввода.
#     '''
#     while True:
#         try:
#             num = int(input(f'Игрок {Player} сколько конфет от {min_cand} до {max_cand} вы возьмете: '))
#             if num <= max_cand and num >= min_cand and num <= num_cand:
#                 break
#             else:
#                 print('Вы ввели не корректное значение!')
#         except ValueError:
#             print('Вы ввели не число!')
#     return num

# def input_bot(min_cand, max_cand, num_cand):
#     '''
#     Функция осуществляет ход бота. 
    
#     '''
#     while True:
#         num = random.randint(min_cand, max_cand)
#         if num <= num_cand:
#             break
#     return num

# def input_bot_intel(min_cand, max_cand, num_cand, num):
#     '''
#     Функция осуществляет ход бота, наделенного "интелектом" 
#     '''    
#     if num_cand % (max_cand + min_cand) !=0 and num_cand > (max_cand + min_cand):
#         num = num_cand % (max_cand + min_cand)
#     else:
#         num = max_cand + min_cand - num
#     return num    


# num_cand = input_number()
# max_cand = input_max(num_cand)
# min_cand = input_min(max_cand)



# Игра между двумя игроками


# while num_cand > 0:
#     num = input_num(min_cand, max_cand, num_cand, 1)       
#     num_cand -= num
#     if num_cand <= 0:
#         win = 'Игрок 1'
#         break
#     print(f'Осталось конфет: {num_cand}')

#     num = input_num(min_cand, max_cand, num_cand, 2)       
#     num_cand -= num
#     if num_cand <= 0:
#         win = 'Игрок 2'
#         break
#     print(f'Осталось конфет: {num_cand}')
# print(f'Победил: {win}')       

import random

# Игра против бота. Бот не наделен интелектом.

# beginning = random.randint(1, 2)
# if beginning == 1:
#     print('Вы играете первым!')

#     while num_cand > 0:
#         num = input_num(min_cand, max_cand, num_cand, 1)       
#         num_cand -= num
#         if num_cand <= 0:
#             win = 'Игрок 1'
#             break
#         print(f'Осталось конфет: {num_cand}')
#         num = input_bot(min_cand, max_cand, num_cand)
#         print(f'Бот взял: {num}')
#         num_cand -= num
#         if num_cand <= 0:
#             win = 'Бот'
#             break
#         print(f'Осталось конфет: {num_cand}')
# else:
#     print('Первым играет Бот')
#     while num_cand > 0:
#         num = input_bot(min_cand, max_cand, num_cand)
#         print(f'Бот взял: {num}')
#         num_cand -= num
#         if num_cand == 0:
#             win = 'Бот'
#             break
#         print(f'Осталось конфет: {num_cand}')
#         num = input_num(min_cand, max_cand, num_cand, 1)       
#         num_cand -= num
#         if num_cand <= 0:
#             win = 'Игрок 1'
#             break
#         print(f'Осталось конфет: {num_cand}')
        
# print(f'Победил: {win}')




# Игра против бота. Бот наделен интелектом.


# beginning = random.randint(1, 2)
# if beginning == 1:
#     print('Вы играете первым!')

#     while num_cand > 0:
#         num = input_num(min_cand, max_cand, num_cand, 1)          
#         num_cand -= num
#         if num_cand <= 0:
#             win = 'Игрок 1'
#             break
#         print(f'Осталось конфет: {num_cand}')
#         num = input_bot_intel(min_cand, max_cand, num_cand, num)
#         print(f'Бот взял: {num}')
#         num_cand -= num
#         if num_cand <= 0:
#             win = 'Бот'
#             break
#         print(f'Осталось конфет: {num_cand}')
# else:
#     print('Первым играет Бот')
#     num = 0
#     while num_cand > 0:
#         num = input_bot_intel(min_cand, max_cand, num_cand, num)
#         print(f'Бот взял: {num}')
#         num_cand -= num
#         if num_cand == 0:
#             win = 'Бот'
#             break
#         print(f'Осталось конфет: {num_cand}')
#         num = input_num(min_cand, max_cand, num_cand, 1)
#         num_cand -= num
#         if num_cand <= 0:
#             win = 'Игрок 1'
#             break
#         print(f'Осталось конфет: {num_cand}')
        
# print(f'Победил: {win}')



# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#'] # [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
#  написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
#  Порядковые номера смотрите в этой таблице, в третьем столбце:

list_languages = ['python', 'c#', 'c++', 'JavaScript', 'Java', 'Fortran']
list_numbers = [i for i in range(1, len(list_languages) + 1)]

def get_list_tuple(list_languages, list_numbers):
    '''
    Функция принимает на вход  список строк и список с номерами и преобразует их в список кортежей 
    из номеров и строк, написанных заглавными буквами. 
    '''
    new_list_languages = [i.upper() for i in list_languages]
    return list(zip(list_numbers, new_list_languages))


def filter(list_tuple):
    '''
    
    '''
    new_list_1 = []
    new_list_2 = []
    for i in list_tuple:
        languages, num = i
        sum = 0
        for j in languages:
            sum += ord(j)
        if  sum % num == 0:
            new_list_1.append(sum)
            new_list_2.append(languages)
    new_list_tuple = list(zip(new_list_1, new_list_2))
    return new_list_tuple

list_tuple = get_list_tuple(list_languages, list_numbers)
print(filter(list_tuple))