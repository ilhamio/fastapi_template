from dependency_injector import containers, providers

from .user import User

__all__ = ["Repository"]


class Repository(containers.DeclarativeContainer):
    user = providers.Factory(User)
