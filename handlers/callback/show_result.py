import re
from api_client.models.game_result import GameResultElement
from api_client.models.user import User
from api_client.api_client import ApiClient, BaseResponseModel
from aiogram import types
import typing
from api_client.models.game_type import GameType
from handlers.buttons.select_category import select_category_keyb
from handlers.buttons.start import start_keyb

async def show_result(query: types.CallbackQuery, user:User, callback_data: dict, client: ApiClient, _: dict):
    game_id = int(callback_data['game_id'])
    game_result : BaseResponseModel[typing.List[GameResultElement]] = await client.get_game_result(game_id)
    text = _["game_result"] + "\n"
    scores = {}
    winner = ""
    if game_result.model:
        for result in game_result.model:
            score = scores.get(result.user.name, None)
            if score != None:
                if result.is_true:
                    scores[result.user.name] += 1
            else:
                if result.is_true:
                    scores[result.user.name] = 1
                else:
                    scores[result.user.name] = 0
        for key, score in scores.items():
            text += key + ": " + str(score) + "\n"
        text += "Вы победили.\nВаш рейтинг повышен с 1920(+94) до 2016.\n"
        text += _["please_start_new_game"]
        await query.message.answer(text, reply_markup=start_keyb(_["start_game_button"]))
            

