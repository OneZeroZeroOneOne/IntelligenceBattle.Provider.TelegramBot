import datetime
import os
from enum import Enum

START_TIME = datetime.datetime.now()

api_client_url = "http://185.87.48.116/api/"

provider_key = "123123123123"

bot_token = "1763731047:AAEcHDkN3gyNeUD4zY_7P2pWGpurxbJhiFo"

TOKEN = os.environ.get('TOKEN')



texts = {
    'ru': {
        'hello': "Здравствуйте, это бот-интеллектуальный баттл, что бы начать нажмите кнопку внизу",
        "select_game_type": "Выберите тип игры:",
        "game_type_info_template": "{title}, кол-во игроков: {count}",
        "start_game_button": "Начать игру",
        "category_info_template": "{title}",
        "select_category": "Выберите категорию",
        "game_started": "игра начата ",
        "error_search": "ошибка поиска",
        "cancel_search": "Отменить",
        "canceled_search": "поиск отменен",
        "question_not_current": "вопрос не является текущим",
        "right": "Правильно",
        "wrong": "Не правильно",
        "game_already_searches": "на даный момент вы уже исчете игру",
        "game_result" : "Результат:",
        "please_start_new_game": "Начните новую игру уже сейчас!",
        "choose_lang": "Выберите свой язык",
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
    ru = 2
    en = 1

DEFAULT_LANG = Lang.en
