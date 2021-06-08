from handlers.buttons.start import start_keyb
from api_client.models.user import User
from api_client.api_client import ApiClient
from aiogram import types
import typing
from api_client.models.game_type import GameType
from config import texts, Lang


async def choosed_lang(query: types.CallbackQuery, callback_data: dict, user: User,client: ApiClient, _: dict):
    lang_id = int(callback_data['lang_id'])
    await client.set_user_lang(lang_id)
    await query.message.answer(texts[Lang(lang_id).name]['hello'], reply_markup=start_keyb(texts[Lang(lang_id).name]["start_game_button"]))
            

