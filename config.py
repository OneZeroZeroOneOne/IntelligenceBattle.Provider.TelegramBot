import datetime
import os
from enum import Enum

START_TIME = datetime.datetime.now()

api_client_url = "http://185.169.252.189/api/"

provider_key = "123123123123"

bot_token = "1763731047:AAEcHDkN3gyNeUD4zY_7P2pWGpurxbJhiFo"



texts = {
    'ua': {
        'hello': "Привіт, це бот-інтелектуальний баттл, щоб почати натисніть кнопку внизу",
        "select_game_type": "Виберіть тип гри:",
        "game_type_info_template": "{title}, кількість гравців: {count}",
        "start_game_button": "Розпочати гру",
        "category_info_template": "{title}",
        "select_category": "Виберіть категорію",
        "game_started": "гра розпочата",
        "error_search": "помилка пошуку",
        "cancel_search": "Відмінити",
        "canceled_search": "пошук відмінений",
        "question_not_current": "питання не є поточним",
        "right": "Правильно",
        "wrong": "Неправильно",
        "game_already_searches": "на даний момент ви вже шукаєте гру",
        "game_result" : "Результат:",
        "please_start_new_game": "Почніть нову гру вже зараз!",
        "choose_lang": "Виберіть свою мову",
    },
    'en': {
        'hello': "Hello",
        "select_game_type": "Select game type:",
        "game_type_info_template": "{title}, player count: {count}",
        "start_game_button": "Start game",
        "select_category": "Please select category:",
        "category_info_template": "{title}",
        "game_started": "game started",
        "error_search": "error_search",
        "cancel_search": "Cancel",
        "canceled_search": "search canceled",
        "question_not_current": "question_not_current",
        "right": "right",
        "wrong": "wrong",
        "game_already_searches": "game already searches",
        "game_result" : "game_result",
        "please_start_new_game": "please_start_new_game",
        "choose_lang": "Choose you language",
    }
}

class Lang(Enum):
    ua = 2
    en = 1

DEFAULT_LANG = Lang.en
