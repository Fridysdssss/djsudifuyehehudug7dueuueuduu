import telebot
import sqlite3 as sq

import Config as cfg
import DataBase as db

bot=telebot.TeleBot('5386732687:AAGuTM9bbuhT_M18DRiKziYvvwl6_dnF0Dc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id,f'💠Привет\n💲Баланс: {db.Balance(message)}')

@bot.message_handler(commands=['give'])
def give_money(message):
    if message.from_user.id==cfg.AdminID:
        try:
            db.give(message)
            bot.send_message(message.from_user.id,f'Вы выдали пользователю денег')
        except:
            bot.send_message(message.from_user.id,f'Не верный формат')

bot.polling()