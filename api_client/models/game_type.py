# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = game_type_from_dict(json.loads(json_string))

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
    game_type_id: int
    lang_id: int
    title: str
    lang_code: str

    def __init__(self, game_type_id: int, lang_id: int, title: str, lang_code: str) -> None:
        self.game_type_id = game_type_id
        self.lang_id = lang_id
        self.title = title
        self.lang_code = lang_code

    @staticmethod
    def from_dict(obj: Any) -> 'Translation':
        assert isinstance(obj, dict)
        game_type_id = from_int(obj.get("gameTypeId"))
        lang_id = from_int(obj.get("langId"))
        title = from_str(obj.get("title"))
        lang_code = from_str(obj.get("langCode"))
        return Translation(game_type_id, lang_id, title, lang_code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["gameTypeId"] = from_int(self.game_type_id)
        result["langId"] = from_int(self.lang_id)
        result["title"] = from_str(self.title)
        result["langCode"] = from_str(self.lang_code)
        return result


class GameType:
    id: int
    title: str
    player_count: int
    translations: List[Translation]

    def __init__(self, id: int, title: str, player_count: int, translations: List[Translation]) -> None:
        self.id = id
        self.title = title
        self.player_count = player_count
        self.translations = translations

    @staticmethod
    def from_dict(obj: Any) -> 'GameType':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        title = from_str(obj.get("title"))
        player_count = from_int(obj.get("playerCount"))
        translations = from_list(Translation.from_dict, obj.get("translations"))
        return GameType(id, title, player_count, translations)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["title"] = from_str(self.title)
        result["playerCount"] = from_int(self.player_count)
        result["translations"] = from_list(lambda x: to_class(Translation, x), self.translations)
        return result


def game_type_from_dict(s: Any) -> GameType:
    return GameType.from_dict(s)


def game_type_to_dict(x: GameType) -> Any:
    return to_class(GameType, x)
