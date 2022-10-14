
from datetime import datetime as dt
from datetime import time
from encodings import utf_8

def start_logger():
    '''
    ф фиксирует время запуска программы
    '''

    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};start;\n'
                    .format(time))


def input_str_logger(data):
    '''
    ф фиксирует время ввода и введённые данные
    '''

    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};input_value;{}\n'
                    .format(time, data))

def input_ok_logger():
    '''
    ф фиксирует время добавления записи в базу данных
    '''

    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};Запись добавлена;\n'
                    .format(time))


def action_logger(data):
    '''
    ф фиксирует время и выбранную команду
    '''
    
    if data == 1:
        data  = 'Поиск'
    elif data == 2:
        data  = 'Добавить запись'
    elif data == 3:
        data  = 'Импорт данных'
    elif data == 4:
        data  = 'Экспорт данных'
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a',  encoding='utf-8') as file:
        file.write('{};function; "{}"\n'
                    .format(time, data))


