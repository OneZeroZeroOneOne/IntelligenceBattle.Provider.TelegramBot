

from api_client.api_client import ApiClient
from aiogram import types



async def cancel_search(query: types.CallbackQuery, callback_data: dict, client: ApiClient, _: dict):
    await client.stop_search(int(callback_data['search_id']))
    await query.message.answer(_["canceled_search"])
            


async def cancel_all_search(query: types.CallbackQuery, client: ApiClient, _: dict):
    await client.stop_all_search()
    await query.message.answer(_["canceled_search"])
            
