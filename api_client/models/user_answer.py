# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = user_answer_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class UserAnswer:
    is_true: bool

    def __init__(self, is_true: bool) -> None:
        self.is_true = is_true

    @staticmethod
    def from_dict(obj: Any) -> 'UserAnswer':
        assert isinstance(obj, dict)
        is_true = from_bool(obj.get("isTrue"))
        return UserAnswer(is_true)

    def to_dict(self) -> dict:
        result: dict = {}
        result["isTrue"] = from_bool(self.is_true)
        return result


def user_answer_from_dict(s: Any) -> UserAnswer:
    return UserAnswer.from_dict(s)


def user_answer_to_dict(x: UserAnswer) -> Any:
    return to_class(UserAnswer, x)
