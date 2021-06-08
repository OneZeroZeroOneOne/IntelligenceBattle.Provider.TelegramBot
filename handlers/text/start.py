from api_client.api_client import ApiClient
from aiogram import types
from handlers.buttons.choose_lang_keyb import choose_lang_keyb


async def start_cmd(message: types.Message, user ,client: ApiClient, _: dict):
    langs_resp = await client.get_langs()
    if langs_resp.model:
        await message.answer(_["choose_lang"], reply_markup=choose_lang_keyb(langs_resp.model))
    elif  langs_resp.error:
        await message.answer(langs_resp.error.Message)