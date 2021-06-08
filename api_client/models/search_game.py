# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = game_search_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class GameSearch:
    id: int
    game_type_id: int
    category_id: int
    user_id: int
    provider_id: int

    def __init__(self, id: int, game_type_id: int, category_id: int, user_id: int, provider_id: int) -> None:
        self.id = id
        self.game_type_id = game_type_id
        self.category_id = category_id
        self.user_id = user_id
        self.provider_id = provider_id

    @staticmethod
    def from_dict(obj: Any) -> 'GameSearch':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        game_type_id = from_int(obj.get("gameTypeId"))
        category_id = from_int(obj.get("categoryId"))
        user_id = from_int(obj.get("userId"))
        provider_id = from_int(obj.get("providerId"))
        return GameSearch(id, game_type_id, category_id, user_id, provider_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["gameTypeId"] = from_int(self.game_type_id)
        result["categoryId"] = from_int(self.category_id)
        result["userId"] = from_int(self.user_id)
        result["providerId"] = from_int(self.provider_id)
        return result


def game_search_from_dict(s: Any) -> GameSearch:
    return GameSearch.from_dict(s)


def game_search_to_dict(x: GameSearch) -> Any:
    return to_class(GameSearch, x)
