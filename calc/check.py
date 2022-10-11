import UI
def check_number():
    '''
    Функция принимает от пользователя  число.
    Производит проверку на корректность ввода.
    '''
    while True:
        try:
            value = UI.get_value()
            break
        except ValueError:
            print('Вы ввели не число!')
    return value  

def check_operation():
    '''
    Функция принимает от пользователя  номер действия.
    Производит проверку на корректность ввода.
    '''
    while True:
        try:
            operation = UI.get_operation()
            if operation > 0 and operation < 5:
                break
            else:
                print('Вы ввели не корректное значение!')
        except ValueError:
            print('Вы ввели не число!')
    return operation  