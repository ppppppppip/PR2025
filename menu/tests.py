import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('7635266212:AAHq0YyK1Zqzj__fMEIzolFc5GH3AnWU9KU')

manager_chat_id = '-4887487352'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Посмотреть меню')
    markup.row(btn2)
    btn3 = types.KeyboardButton('Акции и скидки')
    markup.row(btn3)
    btn4 = types.KeyboardButton('Адреса и время работы')
    markup.row(btn4)
    btn5 = types.KeyboardButton('Связаться с менеджером')
    markup.row(btn5)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


@bot.message_handler(func=lambda message: True)
def on_click(message):
    if message.text == 'Перейти на сайт':
        webbrowser.open('http://127.0.0.1:8000/')
    elif message.text == 'Посмотреть меню':
        bot.reply_to(message, 'Вот наше меню, также советуем посмотреть наши акции!')
        image = [
            'закуски.png',
            'завтрак.png',
            'десерт.png',
            'напитки.png',
            'горячее.jpg',
            'салат.png'
        ]
        for img in image:
            try:
                with open('./' + img, 'rb') as file:
                    bot.send_photo(message.chat.id, file)
            except FileNotFoundError:
                bot.send_message(message.chat.id, f"Файл {img} не найден")
    elif message.text == 'Акции и скидки':
        bot.send_message(message.chat.id, "В нашем ресторане доступны скидки в день рождения(при предъявлении паспорта или других документов, удостоверяющих личность)")
    elif message.text == 'Адреса и время работы':
        bot.send_message(message.chat.id, """г.Москваб ул. Иситовна, д.2б
        пн-сб: 9.00 - 23.00
        вс-выходной""")
    elif message.text == 'Связаться с менеджером':
        bot.send_message(message.chat.id, "Ваше сообщение будет передано менеджеру. \
                                              \nВведите ваш вопрос или сообщение:")
        bot.register_next_step_handler(message, handle_manager_message)
    else:
        bot.send_message(message.chat.id, "Я не понимаю ваш запрос.")


def handle_manager_message(message):
    user_message = message.text
    user_info = f"Пользователь: @{message.from_user.username} (ID: {message.from_user.id})\n" \
                f"Сообщение: {user_message}"

    send_message_to_manager(manager_chat_id, user_info)

    bot.send_message(message.chat.id, "Ваше сообщение успешно отправлено менеджеру. \
                                            \nМы свяжемся с вами в ближайшее время.")


def send_message_to_manager(chat_id, message):
    try:
        bot.send_message(chat_id, message)
    except Exception as e:
        print(f"Ошибка при отправке сообщения менеджеру: {e}")


bot.polling(none_stop=True)
