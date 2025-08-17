import telebot
from telebot import types
from dotenv import load_dotenv
import os

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('English', callback_data='english')
    btn2 = types.InlineKeyboardButton('Russian', callback_data='russian')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Let's get started! Choose the language:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.data == 'english':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Abs', callback_data='abs')
        btn2 = types.InlineKeyboardButton('Glutes', callback_data='glutes')
        btn3 = types.InlineKeyboardButton('Back', callback_data='back')
        btn4 = types.InlineKeyboardButton('Chest', callback_data='chest')
        btn5 = types.InlineKeyboardButton('Biceps', callback_data='biceps')
        btn6 = types.InlineKeyboardButton('Triceps', callback_data='triceps')
        btn7 = types.InlineKeyboardButton('Deltoids', callback_data='deltoids')
        btn8 = types.InlineKeyboardButton('Forearms', callback_data='forearms')
        btn9 = types.InlineKeyboardButton('Quadriceps', callback_data='quadriceps')
        btn10 = types.InlineKeyboardButton('Hamstrings', callback_data='hamstrings')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn6)
        markup.row(btn7, btn8)
        markup.row(btn9, btn10)
        bot.send_message(call.message.chat.id, 'Welcome to your personal <b><em>fitness assistant</em></b>!💪\n\nThis bot will help you quickly find the technique for the exercise you need🏋\nSo you won’t have to waste time looking for videos anymore🕓', parse_mode='HTML')
        bot.send_message(call.message.chat.id, 'Select a muscle group to get exercise options for it, or enter the name of the exercise you’re interested in👇', reply_markup=markup)
    elif call.data == 'russian':
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Пресс', callback_data='abs')
        btn2 = types.InlineKeyboardButton('Ягодицы', callback_data='glutes')
        btn3 = types.InlineKeyboardButton('Спина', callback_data='back')
        btn4 = types.InlineKeyboardButton('Грудные мышцы ', callback_data='chest')
        btn5 = types.InlineKeyboardButton('Бицепс', callback_data='biceps')
        btn6 = types.InlineKeyboardButton('Трицепс', callback_data='triceps')
        btn7 = types.InlineKeyboardButton('Плечи', callback_data='deltoids')
        btn8 = types.InlineKeyboardButton('Предплечья', callback_data='forearms')
        btn9 = types.InlineKeyboardButton('Квадрицепсы', callback_data='quadriceps')
        btn10 = types.InlineKeyboardButton('Задняя поверхность бедра', callback_data='hamstrings')
        markup.row(btn1, btn2)
        markup.row(btn3, btn4)
        markup.row(btn5, btn6)
        markup.row(btn7, btn8)
        markup.row(btn9, btn10)
        bot.send_message(call.message.chat.id, 'Добро пожаловать к твоему личному <b><em>фитнес-помощнику</em></b>!💪\n\nЭтот бот поможет быстро найти технику нужного тебе упражнения🏋\nTак что тебе больше не придётся тратить время на поиск видео🕓', parse_mode='HTML')
        bot.send_message(call.message.chat.id, 'Выберите группу мышц, чтобы получить варианты упражнений на неё, или введите название интересующего вас упражнения👇', reply_markup=markup)
    elif call.data == 'abs':
        with open('abs.mp4', 'rb') as abs_file:
            bot.send_video(call.message.chat.id, abs_file)
    elif call.data == 'glutes':
        with open('glutes.mp4', 'rb') as glutes_file:
            bot.send_video(call.message.chat.id, glutes_file)
    elif call.data == 'back':
        with open('back.mp4', 'rb') as back_file:
            bot.send_video(call.message.chat.id, back_file)
    elif call.data == 'chest':
        with open('chest.mp4', 'rb') as chest_file:
            bot.send_video(call.message.chat.id, chest_file)
    elif call.data == 'biceps':
        with open('biceps.mp4', 'rb') as biceps_file:
            bot.send_video(call.message.chat.id, biceps_file)
    elif call.data == 'triceps':
        with open('triceps.mp4', 'rb') as triceps_file:
            bot.send_video(call.message.chat.id, triceps_file)
    elif call.data == 'deltoids':
        with open('deltoids.mp4', 'rb') as deltoids_file:
            bot.send_video(call.message.chat.id, deltoids_file)
    elif call.data == 'forearms':
        with open('forearms.mp4', 'rb') as forearms_file:
            bot.send_video(call.message.chat.id, forearms_file)
    elif call.data == 'quadriceps':
        with open('quadriceps.mp4', 'rb') as quadriceps_file:
            bot.send_video(call.message.chat.id, quadriceps_file)
    elif call.data == 'hamstrings':
        with open('hamstrings.mp4', 'rb') as hamstrings_file:
            bot.send_video(call.message.chat.id, hamstrings_file)


bot.polling(non_stop=True)
