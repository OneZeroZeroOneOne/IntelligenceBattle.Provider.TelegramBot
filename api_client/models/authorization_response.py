# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = authorization_response_from_dict(json.loads(json_string))

from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class AuthorizationResponse:
    user_id: int
    name: str
    token: str

    def __init__(self, user_id: int, name: str, token: str) -> None:
        self.user_id = user_id
        self.name = name
        self.token = token

    @staticmethod
    def from_dict(obj: Any) -> 'AuthorizationResponse':
        assert isinstance(obj, dict)
        user_id = from_int(obj.get("userId"))
        name = from_str(obj.get("name"))
        token = from_str(obj.get("token"))
        return AuthorizationResponse(user_id, name, token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["userId"] = from_int(self.user_id)
        result["name"] = from_str(self.name)
        result["token"] = from_str(self.token)
        return result


def authorization_response_from_dict(s: Any) -> AuthorizationResponse:
    return AuthorizationResponse.from_dict(s)


def authorization_response_to_dict(x: AuthorizationResponse) -> Any:
    return to_class(AuthorizationResponse, x)
