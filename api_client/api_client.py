from api_client.models.lang import lang_from_dict
from api_client.models.game_result import GameResultElement, game_result_from_dict
from api_client.models.user_answer import user_answer_from_dict
from aiogram.types.message import Message
from dataclasses import dataclass
from api_client.models.search_game import GameSearch, game_search_from_dict
import json
from api_client.models.category import category_from_dict
import typing
from api_client.models.game_type import GameType, game_type_from_dict
from api_client.models.authorization_response import authorization_response_from_dict
from api_client.models.user import user_from_dict
from types import TracebackType
from typing import Any, Dict, Optional, Type, Union
from uuid import UUID
from typing import TypeVar, Generic

import aiohttp
from yarl import URL


                
T = TypeVar("T")
            

@dataclass
class ErrorModel:
    exceptionCode: int
    Message: str


class BaseResponseModel(Generic[T]):
    
    error: Optional[ErrorModel] = None
    model: Optional[T] = None

API_VERSION = 1

class ApiClient:
    def __init__(self, provider_key: Union[str, UUID], user_id: int, base_url: URL = URL('http://185.87.48.116/api/')) -> None:
        self._base_url = base_url
        self.provider_key = provider_key
        self._client = aiohttp.ClientSession(raise_for_status=True)
        self.user_id = user_id
        self.def_headers = {
            "Authorization": f"telegram {self.provider_key};RealId={self.user_id}",
            "ProviderToken": f"telegram {self.provider_key}",
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }

    async def close(self) -> None:
        return await self._client.close()

    def _make_url(self, path: str) -> URL:
        return self._base_url / path
    
    async def get_user(self):
        async with self._client.get(self._make_url("User"), raise_for_status=False, headers=self.def_headers) as resp:
            if (resp.status == 200):
                ret = await resp.json()
                return user_from_dict(ret)
            return None
    

    async def register_user(self, username: str):
        async with self._client.post(self._make_url("Register"), raise_for_status=False, headers=self.def_headers, data=json.dumps({
        "name": username,
        "surname": " ",
        "login": " ", 
        "password": " ",
        "realId": self.user_id,
        "providerId": 2
        })) as resp:
            if (resp.status == 200):
                ret = await resp.json()
                return authorization_response_from_dict(ret)
            return None
    
    async def get_game_types(self) -> typing.Optional[typing.List[GameType]]:
        async with self._client.get(self._make_url("Game/GameType"), raise_for_status=False, headers=self.def_headers) as resp:
            if (resp.status == 200):
                ret = await resp.json()
                l = []
                for i in ret:
                    l.append(game_type_from_dict(i))
                return l
            return None
    

    async def get_categories(self) -> typing.Optional[typing.List[GameType]]:
        async with self._client.get(self._make_url("Game/Category"), raise_for_status=False, headers=self.def_headers) as resp:
            if (resp.status == 200):
                ret = await resp.json()
                l = []
                for i in ret:
                    l.append(category_from_dict(i))
                return l
            return None
    

    async def start_search(self, game_type_id, category_id) -> typing.Optional[BaseResponseModel]:
        return await self.make_post_request("Game/SearchGame", game_search_from_dict, data=json.dumps({ "gameTypeId": game_type_id,"categoryId": category_id }), headers=self.def_headers)


    async def stop_search(self, searchId):
        async with self._client.delete(self._make_url(f"Game/SearchGame/{searchId}"), raise_for_status=False, headers=self.def_headers) as resp:
            pass
    
    async def stop_all_search(self):
        async with self._client.delete(self._make_url(f"Game/SearchGame"), raise_for_status=False, headers=self.def_headers) as resp:
            pass

    async def user_answer(self, game_id, question_id, answer_id):
        return await self.make_post_request("Game/UserAnswer", user_answer_from_dict, headers=self.def_headers, data=json.dumps({
        "gameId": game_id,
        "answerId": answer_id,
        "questionId": question_id
        }))

    
    async def get_game_result(self, game_id):
        return await self.make_get_request("Game/Result", game_result_from_dict, headers=self.def_headers, params={"gameId":game_id})


    async def make_post_request(self, url: str, converter, *args, **kwargs) -> BaseResponseModel :
        async with self._client.post(self._make_url(url), *args, raise_for_status=False, **kwargs) as resp:
            brsm = BaseResponseModel()
            if resp.status == 400:
                ret = await resp.json()
                m = ErrorModel(**ret)
                brsm.error = m
            elif resp.status == 200:
                ret = await resp.json()
                brsm.model = converter(ret)
            return brsm

    async def make_get_request(self, url: str, converter, *args, **kwargs) -> BaseResponseModel :
        async with self._client.get(self._make_url(url), *args, raise_for_status=False, **kwargs) as resp:
            brsm = BaseResponseModel()
            if resp.status == 400:
                ret = await resp.json()
                m = ErrorModel(**ret)
                brsm.error = m
            elif resp.status == 200:
                ret = await resp.json()
                brsm.model = converter(ret)
            return brsm
    

    async def set_user_lang(self, lang_id):
        async with self._client.post(self._make_url(f"User/Lang"), raise_for_status=False, headers=self.def_headers, params={"langId":lang_id}) as resp:
            pass
    
    async def get_langs(self):
        return await self.make_get_request("User/Lang", lang_from_dict, headers=self.def_headers)



