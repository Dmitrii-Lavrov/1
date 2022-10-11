def do_it(x, y, operation): 
    '''
    Функция выполняет выбранное арифметическое действие
    '''
    if operation == 1:
        return x * y
    elif operation == 2:
        return x / y
    elif operation == 3:
        return x + y
    elif operation == 4:
        return x - y