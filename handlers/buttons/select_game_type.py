from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.utils.callback_data import CallbackData  

select_game_type_cb = CallbackData("select_game_type_cb", "game_type_id")



def select_game_type_keyb(types, lang_id):
    keyb = InlineKeyboardMarkup()
    for game_type in types:
        trasl = next((i for i in game_type.translations if i.lang_id == lang_id), None,)
        if not trasl:
            trasl = game_type.title
        else:
            trasl = trasl.title
        keyb.add(InlineKeyboardButton(trasl, callback_data=select_game_type_cb.new(game_type_id=game_type.id)))
    return keyb