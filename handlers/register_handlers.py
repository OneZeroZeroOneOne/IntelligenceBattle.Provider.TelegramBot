from handlers.callback.choosed_lang import choosed_lang
from handlers.buttons.choose_lang_keyb import choose_lang_cb
from handlers.callback.user_answer import user_answer
from handlers.buttons.cancel_search import cancel_all_search_cb, cancel_search_cb
from handlers.callback.cancel_search import cancel_all_search, cancel_search
from handlers.callback.start_search_game import start_search_game
from handlers.callback.select_category import select_category
from aiogram import Bot, Dispatcher
from handlers.text.start import start_cmd
from handlers.callback.select_game_type import select_game_type
from handlers.callback.select_category import select_category
from handlers.buttons.select_game_type import select_game_type_cb
from handlers.buttons.select_category import select_category_cb
from handlers.buttons.start import start_keyb_cb
from handlers.buttons.user_andwer import user_answer_cb
from handlers.callback.show_result import show_result
from handlers.buttons.show_result import show_result_cb

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=['start'])
    dp.register_callback_query_handler(select_game_type, text=start_keyb_cb)
    dp.register_callback_query_handler(select_category, select_game_type_cb.filter())
    dp.register_callback_query_handler(start_search_game, select_category_cb.filter())
    dp.register_callback_query_handler(user_answer, user_answer_cb.filter())    

    dp.register_callback_query_handler(cancel_search, cancel_search_cb.filter())
    dp.register_callback_query_handler(cancel_all_search, text=cancel_all_search_cb)
    dp.register_callback_query_handler(show_result, show_result_cb.filter())
    dp.register_callback_query_handler(choosed_lang, choose_lang_cb.filter())