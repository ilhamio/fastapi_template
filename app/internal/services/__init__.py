from dependency_injector import containers, providers

from app.internal.repository.postgresql import Repository
from .user import User


class Services(containers.DeclarativeContainer):

    repository_container = providers.Container(Repository)

    user = providers.Factory(
        User,
        repository_container.user,
    )

