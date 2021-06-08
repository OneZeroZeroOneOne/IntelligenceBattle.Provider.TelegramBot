from typing import Any
from aiogram.types import Update

from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from config import DEFAULT_LANG, Lang, texts


class I18nDataProviderMiddleware(LifetimeControllerMiddleware):
    """
    Database provider middleware middleware
    """
    skip_patterns = ["error", "update"]

    def __init__(self, dp: Dispatcher):
        super(I18nDataProviderMiddleware, self).__init__()
        self.dp = dp

    async def pre_process(self, message: Any, data: dict,):
        data['_'] = texts[Lang(data['user'].lang_id).name]
       