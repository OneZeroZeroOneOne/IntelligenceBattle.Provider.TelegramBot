from api_client.models.user import User
from api_client.api_client import ApiClient
from aiogram import types
import typing
from api_client.models.game_type import GameType
from handlers.buttons.select_game_type import select_game_type_keyb


async def select_game_type(query: types.CallbackQuery, user: User,client: ApiClient, _: dict):
    types = await client.get_game_types()
    text = _["select_game_type"] + "\n"
    for game_type in types:
        trasl = next((i for i in game_type.translations if i.lang_id == user.lang_id), None,)
        if not trasl:
            trasl = game_type.title
        else:
            trasl = trasl.title
        text += _["game_type_info_template"].format(count=game_type.player_count, title=trasl) + "\n"
    await query.message.answer(text, reply_markup=select_game_type_keyb(types, user.lang_id))
            

