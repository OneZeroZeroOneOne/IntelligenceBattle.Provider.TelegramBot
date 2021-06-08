from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.types import CallbackQuery

start_keyb_cb = 'start_game'


def start_keyb(text):
    keyb = InlineKeyboardMarkup()
    keyb.add(InlineKeyboardButton(text, callback_data=start_keyb_cb))
    return keyb