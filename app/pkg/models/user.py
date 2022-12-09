from pydantic.fields import Field
from pydantic.types import PositiveInt

from .base import BaseModel

__all__ = [
    "User",
    "UserFields",
    "CreateUserCommand",
    "ReadAllUsersQuery",
    "ReadUserByIdQuery",
    "UpdateUserCommand",
    "DeleteUserSpecificCommand",
]


class UserFields:
    id = Field(description="User id.", example=2)
    telegram_user_id = Field(description="Telegram user id.", example=122)


class BaseUser(BaseModel):
    """Base model for user."""


class User(BaseUser):
    id: PositiveInt = UserFields.id
    telegram_user_id: PositiveInt = UserFields.telegram_user_id


# Commands.
class CreateUserCommand(BaseUser):
    telegram_user_id: PositiveInt = UserFields.telegram_user_id


class UpdateUserCommand(BaseUser):
    id: PositiveInt = UserFields.id
    telegram_user_id: PositiveInt = UserFields.telegram_user_id


class DeleteUserSpecificCommand(BaseUser):
    id: PositiveInt = UserFields.id


# Query
class ReadAllUsersQuery(BaseUser):
    ...


class ReadUserByIdQuery(BaseUser):
    id: PositiveInt = UserFields.id
