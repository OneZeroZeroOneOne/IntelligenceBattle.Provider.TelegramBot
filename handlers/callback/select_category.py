from api_client.models.user import User
from api_client.api_client import ApiClient
from aiogram import types
import typing
from api_client.models.game_type import GameType
from handlers.buttons.select_category import select_category_keyb


async def select_category(query: types.CallbackQuery, user:User,callback_data: dict, client: ApiClient, _: dict):
    types = await client.get_categories()
    game_type_id = int(callback_data['game_type_id'])
    text = _["select_category"] + "\n"
    for cat in types:
        trasl = next((i for i in cat.translations if i.lang_id == user.lang_id), None,)
        if not trasl:
            trasl = cat.title
        else:
            trasl = trasl.title
        text += _["category_info_template"].format(title=trasl) + "\n"
    await query.message.answer(text, reply_markup=select_category_keyb(types, game_type_id, user.lang_id))
            

