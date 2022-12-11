import telebot

# просто какой-то коммент

bot = telebot.TeleBot('5726793177:AAEZNMA6PPSdK3noMYX-oKkmMKEBpKxIEco')

@bot.message_handler(commands=['stats'])
def get_stats(message):
    bot.send_message(message.chat.id,
                     "Кол-во людей в чате: " + str(bot.get_chat_member_count(message.chat.id)) + "\n" + "Кол-во "
                                                                                                        "админов "
                                                                                                        "в чате: "
                                                                                                        "" +
                     str(len(bot.get_chat_administrators(message.chat.id))))


@bot.message_handler(commands=['leave'])
def making_bot_leave(message):
    bot.send_message(message.chat.id, "Я покидаю вас, мои приспешники!")
    bot.leave_chat(message.chat.id)


@bot.message_handler(commands=['start'])
def hello_message(message):
    bot.send_message(message.chat.id,
                     "Привет! Преподобный обладает следующим функционалом:" + "\n \n" + "Если введешь сначала в "
                                                                                        "сообщении одну "
                                                                                        "из "
                                                                                        "команд:" + "\n" + "/ban" + "\n"
                     + "/unban" + "\n" + "/makeadmin" + "\n" + "а потом user_id через пробел одного из участников, "
                                                               "то с пользователем произойдут соответствующие "
                                                               "изменения.")

@bot.message_handler(commands=['ban'], content_types=['text'])
def ban_user(message):
    bot.ban_chat_member(message.chat.id, user_id=int(message.text[5:]))


@bot.message_handler(commands=['unban'], content_types=['text'])
def unban_user(message):
    bot.unban_chat_member(message.chat.id, user_id=int(message.text[5:]))


@bot.message_handler(content_types=['left_chat_member'])
def getting_people_out_of_chat(message):
    bot.send_message(message.chat.id, text='Пока человечек!')


@bot.message_handler(content_types=['new_chat_members'])
def getting_people_in_chat(message):
    bot.send_message(message.chat.id, text='Привет, лицезрящий преподобного и добро пожаловать в чат! Для '
                                           'взаимодействия введи команду /start')


# @bot.message_handler(content_types=[''])
# def make_user_admin(message):
#     bot.promote_chat_member(message.chat.id, user_id=523301919, can_promote_members=True, can_restrict_members=True,
#                             can_invite_users=True, can_delete_messages=True, can_pin_messages=True,
#                             can_edit_messages=True, can_post_messages=True,
#                             can_change_info=True, can_manage_voice_chats=True)


bot.polling(none_stop=True, interval=0)
