def print_data(data):
    '''
    Функция выводит результат.
    '''
    print(f'Результат = {data}')

def get_value():
    '''
    Функция запрашивает от пользователя  число.
    '''
    return float(input('Введите число = '))

def get_operation():
    '''
    Функция запрашивает от пользователя номер арифметического действия.
    '''
    return int(input('Введите номер арифметического действия: 1 (*), 2 (/), 3 (+), 4 (-)'))