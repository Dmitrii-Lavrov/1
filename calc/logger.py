from datetime import datetime as dt


def logger(x, y, operation, result):
    time = dt.now().strftime('%H:%M')
    if operation == 1:
        k = '*'
    elif operation == 2:
        k = '/'
    elif operation == 3:
        k = '+'
    elif operation == 4:
        k = '-'
    strok = ''
    strok = strok + str(time) + '    ' + str(x) + ' ' + k + ' ' + str(y) + ' = ' + str(result) 
    with open('log.txt', 'a') as file:
        file.write(strok +'\n')