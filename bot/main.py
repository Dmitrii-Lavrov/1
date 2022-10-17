from telegram import  Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler, CallbackQueryHandler
from config import TOKEN
import random
import logging
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

ACTION, NUMBERFIRST, NUMBERSECOND, OPERATION, NUM_MAX_CAND, PLAY_1, PLAY_2 = range(7)

numberone = ''
numbertwo = ''

logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s", datefmt="%Y/%m/%d, %H:%M:%S", encoding='UTF-8')

logger = logging.getLogger(__name__)


def result(x, y, z):
    '''
    Функция производит выбранное пользователем арифметическое действие и возвращает результат.
    '''
    if  z == '0':
        return x + y
    elif  z == '1':
        return x - y
    elif  z == '2':
        return x * y
    return x/y

def start(update, context):
    '''
    Функция приветствует пользователя, создаёт клавиши в телеграмме и предлагает выбрать действие.
    '''
    user = update.message.from_user
    context.bot.send_message(update.effective_chat.id, 'Приветствую вас в телеграмм-боте. Могу предложить на выбор две функции:\n' 
    '1 Калькулятор для вещественных чисел.\n' 
    '2 Игра в конфеты. Выигрывает, тот, кто заберёт последнею конфету(выиграть у меня практически не возможно).')
    board = [[InlineKeyboardButton('Калькулятор', callback_data = '0'), InlineKeyboardButton('Игра в конфеты', callback_data = '1'),]]
    update.message.reply_text('Выбери:', reply_markup=InlineKeyboardMarkup(board))
    logging.info(f'Бот запущен {user.username} id {user.id}')
    return ACTION

def action(update, context):
    '''
    Функция отслеживает какую клавишу нажал пользователь и направляет выполнение программы.
    '''
    act = update.callback_query.data
    if act == '0':
        context.bot.send_message(update.effective_chat.id, "Введи первое число:")
        logging.info('Пользователь выбрал калькулятор')
        return NUMBERFIRST
    if act == '1':
        context.bot.send_message(update.effective_chat.id, "Сколько всего конфет?: ")
        logging.info('Пользователь выбрал игру в конфеты')
        return NUM_MAX_CAND

def num_max_cand(update, context):
    '''
    Функция принимает от пользователя число конфет в игре и проверяет корректность ввода.
    '''
    global num_cand
    try:
        num_cand = int(update.message.text)
        if num_cand < 3:
            context.bot.send_message(update.effective_chat.id, "Слишком мало! Сколько всего конфет?: ")
            logging.error("Пользователь ввел не корректное значение")
            return NUM_MAX_CAND
        else:
            context.bot.send_message(update.effective_chat.id, "Введи максимальное количество конфет, которое можно взять за раз: ")
            logging.info(f'В игре будет {num_cand} конфет')
            return PLAY_1
    except:
        context.bot.send_message(update.effective_chat.id, "Ты ввел не число! Попробуй еще раз!")
        logging.error("Пользователь ввел не корректное значение")
        return NUM_MAX_CAND
   
def check_max(update, context):
    '''
    Функция принимает от пользователя максимальное число конфет которые можно взять и проверяет корректность ввода.
    '''
    global num_cand
    try:
        max_cand = int(update.message.text)
        if max_cand > 2 and max_cand < num_cand:
            logging.info(f'Максимально можно взять {max_cand} конфет')
            return max_cand
        elif max_cand < 2:
            context.bot.send_message(update.effective_chat.id, "Слишком мало! Введи максимальное количество конфет, которое можно взять за раз: ")
            logging.error("Пользователь ввел не корректное значение")
            return play_1
        elif max_cand > num_cand:
            context.bot.send_message(update.effective_chat.id, "Слишком много! Введи максимальное количество конфет, которое можно взять за раз: ")
            logging.error("Пользователь ввел не корректное значение")
            return play_1
    except:
        context.bot.send_message(update.effective_chat.id, "Ты ввел не число! Попробуй еще раз!")
        logging.error("Пользователь ввел не корректное значение")
        return play_1
    
def play_1(update, context):
    '''
    Функция определяет очередность хода. Если первый ход выпадает пользователю, запрашивает у него количество конфет,
    которые он возьмёт. Если первый ход выпадает боту, считает необходимое для дальнейшей победы количество конфет.
    '''
    global max_cand
    global num_cand
    max_cand = check_max(update, context)
    beginning = random.randint(1, 2)
    if beginning == 1:
        logging.info('Первым играет пользователь')
        context.bot.send_message(update.effective_chat.id, f"Вы играете первым! \nСколько конфет от 1 до {max_cand} возьмешь?")
        return PLAY_2
    else: 
        logging.info('Первым играет бот')
        if num_cand % (max_cand + 1) !=0:
            num_bot = num_cand % (max_cand + 1)
        else:
            num_bot = max_cand - 1
            num_cand -= num_bot
        context.bot.send_message(update.effective_chat.id, f"Бот играет первым! \nБот взял {num_bot} \nОсталось {num_cand} Сколько конфет от 1 до {max_cand} возьмешь?")
        logging.info(f'Бот взял {num_bot} Осталось {num_cand}')
        return PLAY_2

def check_num(update, context):
    '''
    Функция проверяет на корректность ввода.
    '''
    global max_cand
    try:
        num = int(update.message.text)
        if num > max_cand:
            context.bot.send_message(update.effective_chat.id, f"Ты жульничаешь! Сколько конфет от 1 до {max_cand} возьмешь?")
            logging.error("Пользователь ввел не корректное значение")
            return play_2
        elif num > num_cand:
            context.bot.send_message(update.effective_chat.id, "Ну нет же столько конфет! Попробуй еще раз!")
            logging.error("Пользователь ввел не корректное значение")
            return play_2  
        elif num < 1:
            context.bot.send_message(update.effective_chat.id, f"Надо взять, хотя бы одну конфету! Сколько конфет от 1 до {max_cand} возьмешь?")
            logging.error("Пользователь ввел не корректное значение")
            return play_2         
        return num
    except:
        context.bot.send_message(update.effective_chat.id, "Ты ввел не число! Попробуй еще раз!")
        logging.error("Пользователь ввел не корректное значение")
        return play_2

def play_2(update, context):
    '''
    Функция принимает от пользователя количество конфет которые он взял.Считает сколько осталось конфет. 
    Если конфеты ещё есть, считает сколько конфет возьмёт бот. 
    '''
    global num_cand
    global max_cand
    num = check_num(update, context)
    num_cand -= num
    context.bot.send_message(update.effective_chat.id, f"Ты взял {num} \nОсталось {num_cand}")
    logging.info(f'Пользователь взял {num} Осталось {num_cand}')
    if num_cand <= 0:
        context.bot.send_message(update.effective_chat.id, f"Ты победил!")
        logging.info(f'Победил пользователь')
        context.bot.send_message(update.effective_chat.id, "Если хочешь еще, жми: /start")
        logging.info('Завершение программы')
        return ConversationHandler.END 
        
    else:
        if num_cand % (max_cand + 1) !=0:
            num_bot = num_cand % (max_cand + 1)
        else:
            num_bot = max_cand - 1
    if num_bot >= num_cand:
            num_bot = num_cand
    num_cand -= num_bot            
    if num_cand == 0:
        context.bot.send_message(update.effective_chat.id, f"Бот взял {num_bot} \nОсталось {num_cand} \nБот победил!")
        logging.info(f'Бот взял {num_bot} Осталось {num_cand} Бот победил')
        context.bot.send_message(update.effective_chat.id, "Если хочешь еще, жми: /start")
        logging.info('Завершение программы')
        return ConversationHandler.END 
    context.bot.send_message(update.effective_chat.id, f"Бот взял {num_bot} \nОсталось {num_cand} \nСколько конфет от 1 до {max_cand} возьмешь?")
    logging.info(f'Бот взял {num_bot} Осталось {num_cand}')
    return PLAY_2

def numberFirst(update, context):
    '''
    Функция принимает от пользователя первое число, проверяет на корректность ввода.
    '''
    global numberone
    
    try:
        numberone = float(update.message.text)
        logging.info(f'Пользователь ввел первое число: {numberone}')
        context.bot.send_message(update.effective_chat.id, "Введи второе число: ")
        return NUMBERSECOND
    except:
        context.bot.send_message(update.effective_chat.id, "Ты ввел не число! Попробуй еще раз! Введи первое число: ")
        logging.error("Пользователь ввел не корректное значение")
        return NUMBERFIRST
  
def numberSecond(update, context):
    '''
    Функция принимает от пользователя второе число, проверяет на корректность ввода.
    '''
    global numbertwo
    
    try:    
        numbertwo = float(update.message.text)
        logging.info(f'Пользователь ввел второе число: {numbertwo}')
        board = [[InlineKeyboardButton('+', callback_data = '0'), InlineKeyboardButton('-', callback_data = '1'),
                InlineKeyboardButton('*', callback_data = '2'), InlineKeyboardButton('/', callback_data = '3')]]
        update.message.reply_text('Выбери:', reply_markup=InlineKeyboardMarkup(board))
        return OPERATION
    
    except:
        context.bot.send_message(update.effective_chat.id, "Ты ввел не число! Попробуй еще раз! Введи второе число: ")
        logging.error("Пользователь ввел не корректное значение")
        return NUMBERSECOND

def operation(update, context):
    '''
    Функция отслеживает какую клавишу нажал пользователь
    и вызывает функцию вычисления, согласно выбранного арифметического действия.
    '''
    global res
    var = update.callback_query.data
    if var == '3' and numbertwo == 0:
        context.bot.send_message(update.effective_chat.id, "На ноль делить нельзя! Попробуй еще раз! Введи второе число: ")
        logging.error("Пользователь ввел не корректное значение")
        return NUMBERSECOND
    else:
        res = result(numberone, numbertwo, var)
        update.callback_query.edit_message_text(text=f'Результат: {res}')
        logging.info(f'Результат вычисления: {res}')
        context.bot.send_message(update.effective_chat.id, "Если хочешь еще, жми: /start")
        logging.info('Завершение программы')
        return ConversationHandler.END

def cancel(update, context):
    '''
    Функция принимает от пользователя команду закончить работу и останавливает выполнение программы.
    '''
    context.bot.send_message(update.effective_chat.id, "Пока!")
    logging.info('Завершение программы')
    return ConversationHandler.END

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={ACTION: [CallbackQueryHandler(action)],
            NUM_MAX_CAND: [MessageHandler(Filters.text & ~Filters.command, num_max_cand)],
            NUMBERFIRST: [MessageHandler(Filters.text & ~Filters.command, numberFirst)],
            NUMBERSECOND: [MessageHandler(Filters.text & ~Filters.command, numberSecond)],
            OPERATION: [CallbackQueryHandler(operation)],
            PLAY_1: [MessageHandler(Filters.text & ~Filters.command, play_1)],
            PLAY_2: [MessageHandler(Filters.text & ~Filters.command, play_2)]
            },
    fallbacks=[CommandHandler('cancel', cancel)])

dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()
