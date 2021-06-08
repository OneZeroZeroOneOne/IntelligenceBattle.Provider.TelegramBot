# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = lang_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class LangElement:
    id: int
    code: str

    def __init__(self, id: int, code: str) -> None:
        self.id = id
        self.code = code

    @staticmethod
    def from_dict(obj: Any) -> 'LangElement':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        code = from_str(obj.get("code"))
        return LangElement(id, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["code"] = from_str(self.code)
        return result


def lang_from_dict(s: Any) -> List[LangElement]:
    return from_list(LangElement.from_dict, s)


def lang_to_dict(x: List[LangElement]) -> Any:
    return from_list(lambda x: to_class(LangElement, x), x)
