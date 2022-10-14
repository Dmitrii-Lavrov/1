import ui 
import check
import mod


def button_click():
    '''
    Функция запускает программу.
    '''
    ui.hello()
    deistvie = check.check_action()
    if deistvie == 1:        
        mod.search_number(ui.input_search())
    elif deistvie == 2:
        data = ui.input_data()
        mod.write_number(data[0], data[1], data[2])
        

