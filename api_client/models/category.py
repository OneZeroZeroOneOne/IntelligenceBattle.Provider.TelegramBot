# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = category_from_dict(json.loads(json_string))

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


class Translation:
    category_id: int
    lang_id: int
    title: str
    lang_code: str

    def __init__(self, category_id: int, lang_id: int, title: str, lang_code: str) -> None:
        self.category_id = category_id
        self.lang_id = lang_id
        self.title = title
        self.lang_code = lang_code

    @staticmethod
    def from_dict(obj: Any) -> 'Translation':
        assert isinstance(obj, dict)
        category_id = from_int(obj.get("categoryId"))
        lang_id = from_int(obj.get("langId"))
        title = from_str(obj.get("title"))
        lang_code = from_str(obj.get("langCode"))
        return Translation(category_id, lang_id, title, lang_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["categoryId"] = from_int(self.category_id)
        result["langId"] = from_int(self.lang_id)
        result["title"] = from_str(self.title)
        result["langCode"] = from_str(self.lang_code)
        return result


class Category:
    id: int
    title: str
    translations: List[Translation]

    def __init__(self, id: int, title: str, translations: List[Translation]) -> None:
        self.id = id
        self.title = title
        self.translations = translations

    @staticmethod
    def from_dict(obj: Any) -> 'Category':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        translations = from_list(Translation.from_dict, obj.get("translations"))
        return Category(id, title, translations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["translations"] = from_list(lambda x: to_class(Translation, x), self.translations)
        return result


def category_from_dict(s: Any) -> Category:
    return Category.from_dict(s)


def category_to_dict(x: Category) -> Any:
    return to_class(Category, x)
