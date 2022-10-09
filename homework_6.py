from math import sqrt

import re
 
# actions = {
#   "^": lambda x, y: str(float(x)**float(y)),
#   "*": lambda x, y: str(float(x) * float(y)),
#   "/": lambda x, y: str(float(x) / float(y)),
#   "+": lambda x, y: str(float(x) + float(y)),
#   "-": lambda x, y: str(float(x) - float(y))
# }
 
# priority_reg_exp = r"\((.+?)\)"
# action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
# def my_eval(expresion: str) -> str:
 
#     while (match := re.search(priority_reg_exp, expresion)):
#         expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))
 
#     for symbol, action in actions.items():
#         while (match := re.search(action_reg_exp.format(symbol), expresion)):
#             expresion: str = expresion.replace(match.group(0), action(*match.groups()))
 
#     return expresion
 
 
# exp = "(1 + 5) * (5 * (18 - 2)) / 5"
# print(my_eval(exp), eval(exp))


#####################################################################



#  Определить, присутствует ли в заданном списке строк, некоторое число

# data = ['iuh8', 'jhhb7', 'iuh6', 'uih1']
# num = 1
# print(any(str(num) in i for i in data))


########################################################################



#  Найти сумму чисел списка стоящих на нечетной позиции

# data = [1, 3, 4, 5, 8, 3, 9]
# print(sum(data[1::2]))


#############################################################



# Найти расстояние между двумя точками пространства(числа вводятся через пробел)


# p1 = list(map(int, input('Введите координаты первой точки через пробел: ').split(' ')))
# p2 = list(map(int, input('Введите координаты второй точки через пробел: ').split(' ')))
# length = round(sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2), 2)
# print(f'Расстояние между точками: {length}')


#############################################################



# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.

# data = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# str = 'qwe'
# data_1 = list(enumerate(data))
# print(data_1)
# sort_data = list(filter(lambda x: str in x, data_1))
# print(sort_data)
# if len(sort_data) > 1:
#     print(sort_data[1][0])
# else:
#     print(-1)


###############################################




#  Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
 
# import math
# list_num =[1, 2, 3, 4, 5, 6, 7, 8]
# prod_list = []
# for i in range(math.ceil(len(list_num)/2)):
#     prod_list.append(list_num[i] * list_num[-i-1])
# print(prod_list)



################################################


# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

N = 5
data = [(-3)**i for i in range(N)] 
print(data)