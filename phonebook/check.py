import ui

def check_action():
    '''
    Функция принимает от пользователя  номер действия.
    Производит проверку на корректность ввода.
    '''
    while True:
        try:
            deistvie = ui.action()
            if deistvie > 0 and deistvie < 3:
                break
            else:
                print('Вы ввели не корректное значение!')
        except ValueError:
            print('Вы ввели не число!')
    return deistvie  

