import telebot

TOKEN = '826161378:AAFsLX7EJwPlNfAH31cSoK7MeW3MUP_uqKQ'
bot = telebot.TeleBot(TOKEN)


def send_nudes(data):    # after getting nudes (data), make request to parent
    user_name = data["user_name"]
    task = data["task"]
    user_id = data['user_id']
    bot.send_message(user_id, 'Task ' + task + ' is completed by ' + user_name)
    """
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Yeah', 'No')
    bot.send_message(user_id, user_name + ' finished ' + task + '\nConfirm?', reply_markup=user_markup)
    """


def send_nudes0(data):    # after creating nudes (data)
    user_name = data["user_name"]
    task = data["task"]
    user_id = data['user_id']
    deadline = data['deadline']
    bot.send_message(user_id, 'Task ' + task + ' is set by ' + user_name + '\nDeadline: ' + deadline)
    """
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('Yeah', 'No')
    bot.send_message(user_id, user_name + ' finished ' + task + '\nConfirm?', reply_markup=user_markup)
    """