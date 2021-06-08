


from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

cancel_search_cb = CallbackData("cancel_search_cb", "search_id")

cancel_all_search_cb = "cancel_all_search_cb"


def cancel_search_keyb(but_title, search_id):
    keyb = InlineKeyboardMarkup()
    keyb.add(InlineKeyboardButton(but_title, callback_data=cancel_search_cb.new(search_id=search_id)))
    return keyb


def cancel_all_search_keyb(but_title):
    keyb = InlineKeyboardMarkup()
    keyb.add(InlineKeyboardButton(but_title, callback_data=cancel_all_search_cb))
    return keyb