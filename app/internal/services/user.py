"""User service."""
from typing import List, Optional

from app.internal.repository.postgresql import user
from app.internal.repository.repository import BaseRepository
from app.pkg import models
from app.pkg.models.exceptions.repository import UniqueViolation
from app.pkg.models.exceptions.user import UserAlreadyExist

__all__ = ["User"]


class User:
    repository: user.User

    def __init__(self, repository: BaseRepository):
        self.repository = repository

    async def create_user(self, cmd: models.CreateUserCommand) -> models.User:
        try:
            return await self.repository.create(cmd=cmd)
        except UniqueViolation:
            raise UserAlreadyExist

    async def read_all_users(
        self,
        query: Optional[models.ReadAllUsersQuery] = None,
    ) -> List[models.User]:
        """Read all users from repository."""

        if not query:
            query = models.ReadAllUsersQuery()
        return await self.repository.read_all(query=query)

    async def read_specific_user_by_id(
        self,
        query: models.ReadUserByIdQuery,
    ) -> models.User:
        """Read specific user from repository by user id."""

        return await self.repository.read(query=query)

    async def delete_specific_user(
        self,
        cmd: models.DeleteUserSpecificCommand,
    ) -> models.User:
        """Delete specific user by user id."""

        return await self.repository.delete(cmd=cmd)
