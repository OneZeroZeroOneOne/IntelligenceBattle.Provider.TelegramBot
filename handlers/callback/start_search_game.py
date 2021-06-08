from handlers.buttons.cancel_search import cancel_all_search_keyb, cancel_search_keyb
from re import search
from api_client.api_client import ApiClient
from aiogram import types
import typing
from api_client.models.game_type import GameType
from handlers.buttons.select_game_type import select_game_type_keyb


async def start_search_game(query: types.CallbackQuery, callback_data:dict, client: ApiClient, _: dict):
    search = await client.start_search(int(callback_data['game_type_id']), int(callback_data['category_id']))
    text = _["game_started"]
    if search.error:
        if search.error.exceptionCode == 16:
            return await query.message.answer(_["game_already_searches"], reply_markup=cancel_all_search_keyb(_["cancel_search"]))

    if search.model:
        await query.message.answer(text, reply_markup=cancel_search_keyb(_["cancel_search"], search.model.id))
    else:
        await query.message.answer(_["error_search"], reply_markup=cancel_all_search_keyb(_["cancel_search"]))
            

