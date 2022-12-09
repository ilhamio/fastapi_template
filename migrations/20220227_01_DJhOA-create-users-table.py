"""
create users table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
            create table if not exists users(
                id serial primary key,
                telegram_user_id int8 unique not null
            )
        """,
        """
            drop table if exists users; 
        """
    ),
]
