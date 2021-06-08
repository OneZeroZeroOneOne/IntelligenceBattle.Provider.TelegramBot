from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

choose_lang_cb = CallbackData("choose_lang_cb", "lang_id")
from api_client.models.lang import LangElement, lang_from_dict
import typing

def choose_lang_keyb(langs: typing.List[LangElement]):
    keyb = InlineKeyboardMarkup()
    for lang in langs:
        keyb.add(InlineKeyboardButton(lang.code, callback_data=choose_lang_cb.new(lang_id=lang.id)))
    return keyb