def write_number(surname, name, num):
    '''
    Функция записи данных в файл. Принимает в качестве аргументов фамилию, имя и номер телефона, присваивает
    ID, формирует строку и записывает в файл.
    '''
    id = get_id() + 1
    entry = ''
    entry += str(id) + ' ' + surname + ' ' + name + ' ' + str(num)    
    with open('phone.txt', 'a', encoding='utf-8') as file:
        file.write(entry + '\n')

def get_id():
    '''
    Функция получает последний ID номер из файла. Если файл пустой возвращает 0. 
    '''
    while True:
        try:
            with open('phone.txt', 'r', encoding='utf-8') as file:
                id = int(file.readlines()[-1].split(' ')[0])
            return id
        except IndexError:
            return 0

def search_number(data):
    '''
    Функция осуществляет поиск введенных, пользователем символов в записях в файле. При нахождении 
    совпадений выводит строку на экран. При отсутствии совпадений выводит:
    База данных не содержит такой записи!
    '''
    with open('phone.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:            
            if data in line:
                print(line, end="")
                count += 1
        if count == 0:
            print('База данных не содержит такой записи!')