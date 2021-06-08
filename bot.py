import logging
from middlewares.user_provider_middleware import UserProviderMiddleware

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from middlewares.api_provider_middleware import ApiClientProviderMiddleware
from middlewares.i18n_data_provider_midleware import I18nDataProviderMiddleware
from handlers.register_handlers import register_handlers

logging.basicConfig(level=logging.INFO)

def init_bot(token: str):
    return Bot(token=token, parse_mode='HTML')


def init_dispatcher(bot: Bot):
    storage = MemoryStorage()

    return Dispatcher(bot, storage=storage)


async def on_startup(dp: Dispatcher):
    pass


def start_polling(token: str, api_url: str):
    bot = init_bot(token)
    dp = init_dispatcher(bot)

    dp["api_client_url"] = api_url

    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(ApiClientProviderMiddleware(dp))
    dp.middleware.setup(UserProviderMiddleware(dp))
    dp.middleware.setup(I18nDataProviderMiddleware(dp))
    
    
    register_handlers(dp)

    executor.start_polling(dp, skip_updates=True)

