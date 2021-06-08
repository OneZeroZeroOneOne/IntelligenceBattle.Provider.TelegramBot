# This code parses date/times, so please
#
#     pip install python-dateutil
#
# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = game_result_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, List, TypeVar, Type, cast, Callable
import dateutil.parser


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class User:
    id: int
    name: str
    lang_id: int
    surname: str
    lang_code: str
    created_date_time: datetime

    def __init__(self, id: int, name: str, lang_id: int, surname: str, lang_code: str, created_date_time: datetime) -> None:
        self.id = id
        self.name = name
        self.lang_id = lang_id
        self.surname = surname
        self.lang_code = lang_code
        self.created_date_time = created_date_time

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        lang_id = int(from_str(obj.get("langId")))
        surname = from_str(obj.get("surname"))
        lang_code = from_str(obj.get("langCode"))
        created_date_time = from_datetime(obj.get("createdDateTime"))
        return User(id, name, lang_id, surname, lang_code, created_date_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["langId"] = from_str(str(self.lang_id))
        result["surname"] = from_str(self.surname)
        result["langCode"] = from_none(self.lang_code)
        result["createdDateTime"] = self.created_date_time.isoformat()
        return result


class GameResultElement:
    user: User
    is_true: bool

    def __init__(self, user: User, is_true: bool) -> None:
        self.user = user
        self.is_true = is_true

    @staticmethod
    def from_dict(obj: Any) -> 'GameResultElement':
        assert isinstance(obj, dict)
        user = User.from_dict(obj.get("user"))
        is_true = from_bool(obj.get("isTrue"))
        return GameResultElement(user, is_true)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = to_class(User, self.user)
        result["isTrue"] = from_bool(self.is_true)
        return result


def game_result_from_dict(s: Any) -> List[GameResultElement]:
    return from_list(GameResultElement.from_dict, s)


def game_result_to_dict(x: List[GameResultElement]) -> Any:
    return from_list(lambda x: to_class(GameResultElement, x), x)
