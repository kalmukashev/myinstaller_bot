import telebot;
bot = telebot.TeleBot('1568454094:AAGOrnW1-ZMg3FotikzBG4Ks-GvGoSTvlhg');
from telebot import types

hey = ["привет", "здравствуй", "hi", "hello", "helloy", "добрый ранок", "доброго ранку", "ghbdtn"]

def create_keyboard1():
	keyboard = types.InlineKeyboardMarkup()
	word_btn = types.InlineKeyboardButton(text = "Word", url="https://word-load.com")
	excel_btn = types.InlineKeyboardButton(text = "Excel", url="https://excel-load.com")
	python_btn = types.InlineKeyboardButton(text = "Python", url="https://www.python.org")
	c_btn = types.InlineKeyboardButton(text = "C++", url="https://acmp.ru/article.asp?id_text=845")
	help_btn = types.InlineKeyboardButton(text = "Донат", url="https://www.donationalerts.com/r/kalmukashev")
	windows_btn = types.InlineKeyboardButton(text = "Windows", url="https://www.microsoft.com/ru-ru/software-download/windows10")
	opera_btn = types.InlineKeyboardButton(text = "Opera GX", url="https://www.opera.com/ru/gx")
	keyboard.add(word_btn)
	keyboard.add(excel_btn)
	keyboard.add(python_btn)
	keyboard.add(c_btn)
	keyboard.add(windows_btn)
	keyboard.add(help_btn)
	return keyboard

def create_keyboard2():
	keyboard = types.InlineKeyboardMarkup()
	vk_btn = types.InlineKeyboardButton(text = "Вконтакте", url="https://vk.com")
	insta_btn = types.InlineKeyboardButton(text = "Instagram", url="https://www.instagram.com")
	faceb_btn = types.InlineKeyboardButton(text = "Facebook", url="https://www.facebook.com")
	twitter_btn = types.InlineKeyboardButton(text = "Twitter", url="https://twitter.com")
	yout_btn = types.InlineKeyboardButton(text = "Youtube", url="https://www.youtube.com")
	twitch_btn = types.InlineKeyboardButton(text = "Twitch", url="https://www.twitch.tv")
	keyboard.add(vk_btn)
	keyboard.add(insta_btn)
	keyboard.add(faceb_btn)
	keyboard.add(twitter_btn)
	keyboard.add(yout_btn)
	keyboard.add(twitch_btn)
	return keyboard

def create_keyboard3():
	keyboard = types.InlineKeyboardMarkup()
	acmp_btn = types.InlineKeyboardButton(text = "Школа Программиста(acmp)", url="https://acmp.ru")
	stepik_btn = types.InlineKeyboardButton(text = "Stepik", url="https://stepik.org")
	keyboard.add(acmp_btn)
	keyboard.add(stepik_btn)
	return keyboard

@bot.message_handler(content_types=['text'])
def get_download(message):
	if message.text.lower() in hey:
		bot.send_message(message.chat.id, "Привет! Если тебе что-то надо, то пропиши /help")
	if message.text == 'Скачать' or message.text == 'скачать':
		bot.send_message(message.chat.id, "Какой товар вам нужен? выбери из списка ниже и тыкни по ней.", reply_markup=create_keyboard1())
	if message.text == 'Ссылки' or message.text == 'ссылки':
		bot.send_message(message.chat.id, "Вот список доступных ссылок:", reply_markup=create_keyboard2())
	if message.text == 'Задачки' or message.text == 'задачки':
		bot.send_message(message.chat.id, "Вот где можно позаниматься программированием:", reply_markup=create_keyboard3())
	if message.text.lower() not in hey and message.text != 'Скачать' and message.text != 'скачать' and message.text != '/help' and message.text != 'Ссылки' and message.text != 'ссылки' and message.text != 'Задачки' and message.text != 'задачки':
		bot.send_message(message.chat.id, "У вас ошибка! Введи /help и пиши, то что там написано, спасибо за понимание.")
	if message.text == '/help':
		bot.send_message(message.chat.id, "1 Команда: Напиши Привет или привет\n2 Команда: Напиши Скачать или скачать\n3 Команда: Напиши Ссылки или ссылки\n4 Команда: Напиши Задачки или задачки\n")

bot.polling(none_stop=True, interval = 0)
