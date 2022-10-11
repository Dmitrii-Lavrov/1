import  model
import UI
import check
import logger

def button_click():
    x = check.check_number()
    y = check.check_number()
    operation = check.check_operation()
    result = model.do_it(x, y, operation)
    UI.print_data(result)
    logger.logger(x, y, operation, result)