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
#     result = user_from_dict(json.loads(json_string))

from datetime import datetime
from typing import Any, TypeVar, Type, cast
import dateutil.parser


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_datetime(x: Any) -> datetime:
    return dateutil.parser.parse(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class User:
    id: int
    name: str
    lang_id: int
    surname: str
    created_date_time: datetime

    def __init__(self, id: int, name: str, lang_id: int, surname: str, created_date_time: datetime) -> None:
        self.id = id
        self.name = name
        self.lang_id = lang_id
        self.surname = surname
        self.created_date_time = created_date_time

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        name = from_str(obj.get("name"))
        lang_id = int(from_str(obj.get("langId")))
        surname = from_str(obj.get("surname"))
        created_date_time = from_datetime(obj.get("createdDateTime"))
        return User(id, name, lang_id, surname, created_date_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["name"] = from_str(self.name)
        result["langId"] = from_str(str(self.lang_id))
        result["surname"] = from_str(self.surname)
        result["createdDateTime"] = self.created_date_time.isoformat()
        return result


def user_from_dict(s: Any) -> User:
    return User.from_dict(s)


def user_to_dict(x: User) -> Any:
    return to_class(User, x)
