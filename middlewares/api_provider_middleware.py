from typing import Any, Union

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from api_client.api_client import  ApiClient
import config
from aiogram import types
from yarl import URL

class ApiClientProviderMiddleware(LifetimeControllerMiddleware):
    """
    Database provider middleware middleware
    """
    skip_patterns = ["error", "update"]
    def __init__(self, dp: Dispatcher):
        super(ApiClientProviderMiddleware, self).__init__()
        self.dp = dp

    async def pre_process(self, message: Union[types.Message, types.CallbackQuery], data: dict,):
        user = None
        if isinstance(message, types.Message):
            user=message.from_user
        elif isinstance(message, types.CallbackQuery):
            user=message.from_user
        data['client'] = ApiClient(config.provider_key, message.from_user.id, URL(self.dp['api_client_url']))

    
    async def post_process(self, obj, data, *args):
        if (data['client']):
            await data['client'].close()
