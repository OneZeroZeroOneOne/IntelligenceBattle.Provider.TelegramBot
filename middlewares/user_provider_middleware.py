
from typing import Any, Union
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from api_client.api_client import  ApiClient
import config
from aiogram import types


class UserProviderMiddleware(LifetimeControllerMiddleware):
    """
    Database provider middleware middleware
    """
    skip_patterns = ["error", "update"]

    def __init__(self, dp: Dispatcher):
        super(UserProviderMiddleware, self).__init__()
        self.dp = dp

    async def pre_process(self, message: Union[types.Message, types.CallbackQuery], data: dict,):
        data['user'] = await data['client'].get_user()
        if not data['user']:
            await data['client'].register_user(message.from_user.username)
            data['user'] = await data['client'].get_user()



    
    async def post_process(self, obj, data, *args):
        if (data['user']):
            data['user'] = None