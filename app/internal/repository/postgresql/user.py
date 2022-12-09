from typing import List

from app.internal.repository.handlers.postgresql.collect_response import (
    collect_response,
)
from app.internal.repository.postgresql.connection import get_connection
from app.internal.repository.repository import Repository
from app.pkg import models

__all__ = ["User"]


class User(Repository):
    @collect_response
    async def create(self, cmd: models.CreateUserCommand) -> models.User:
        q = """
            insert into users(
                telegram_user_id
            )
                values (
                    %(telegram_user_id)s
                )
            returning id, telegram_user_id;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def read(self, query: models.ReadUserByIdQuery) -> models.User:
        q = """
            select 
                id, 
                telegram_user_id
            from users
            where users.id = %(id)s;
        """
        async with get_connection() as cur:
            await cur.execute(q, query.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def read_all(self, query: models.ReadAllUsersQuery) -> List[models.User]:
        q = """
            select 
                id, 
                telegram_user_id
            from users;
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()

    @collect_response
    async def update(self, cmd: models.UpdateUserCommand) -> models.User:
        q = """
            update users 
                set 
                    telegram_user_id = %(telegram_user_id)s
                where id = %(id)s
            returning 
                id, telegram_user_id;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict(show_secrets=True))
            return await cur.fetchone()

    @collect_response
    async def delete(self, cmd: models.DeleteUserSpecificCommand) -> models.User:
        q = """
            delete from users where id = %(id)s
            returning id, telegram_user_id;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict(show_secrets=True))
            return await cur.fetchone()
