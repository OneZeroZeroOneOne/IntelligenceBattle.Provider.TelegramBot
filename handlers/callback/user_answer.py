from re import search
from api_client.api_client import ApiClient
from aiogram import types
import typing
from api_client.models.game_type import GameType


async def user_answer(query: types.CallbackQuery, callback_data:dict, client: ApiClient, _: dict):
    game_id = int(callback_data['game_id'])
    question_id = int(callback_data['question_id'])
    answer_id = int(callback_data['answer_id'])
    search = await client.user_answer(game_id, question_id, answer_id)
    if search.error:
        if search.error.exceptionCode == 19:
            return await query.answer(_["question_not_current"])
    if search.model:
        await query.message.answer(_["right"] if search.model.is_true == True else _["wrong"])
            