from re import A
import data_logger as  dl
from datetime import datetime as dt
from datetime import time
from encodings import utf_8
import json




def hello(): 
    '''
    ф выводит название программы и вызывает логгер_начала работы программы
    '''
    dl.start_logger()
    return print('Программа "справочник"\n') 
 
 
def input_search(): 
    '''
    ф выводит информационную строку и вызывает логгер_поискового запроса
    '''

    data = str(input('Введите поисковый запрос: ')) 
    dl.input_str_logger(data) 
    return data 
 
 
def action():
    '''
    ф выводит в консоль меню выбора действий и вызывает логгер_действий
    '''

    deistvie = int(input('Выберете цифру соответствующую операции и нажмите "ввод"\n 1: "Поиск"\n 2: "Добавить запись"\n 3: "Импорт данных"\n 4:"Экспорт данных"\n')) 
    dl.action_logger(deistvie) 
    return deistvie 
 
def input_data():
    '''
    ф выводит в консоль подсказки и принимает от пользователя данные, вызывает логгер_записи данных
    ''' 

    surname = str(input('Введите фамилию: ')) 
    name = str(input('Введите имя: ')) 
    num = int(input('Введите номер: ')) 
    dl.input_ok_logger()
    return surname, name, num
