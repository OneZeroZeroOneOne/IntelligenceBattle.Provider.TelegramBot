from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

select_category_cb = CallbackData("select_category_cb", "category_id", "game_type_id")



def select_category_keyb(types, game_type_id, lang_id):
    keyb = InlineKeyboardMarkup()
    for cat in types:
        trasl = next((i for i in cat.translations if i.lang_id == lang_id), None,)
        if not trasl:
            trasl = cat.title
        else:
            trasl = trasl.title
        keyb.add(InlineKeyboardButton(trasl, callback_data=select_category_cb.new(category_id=cat.id ,game_type_id=game_type_id)))
    return keyb