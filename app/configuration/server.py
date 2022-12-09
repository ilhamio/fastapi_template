"""Server configuration."""
from typing import TypeVar

from fastapi import FastAPI

from app.internal.routes import __routes__

__all__ = ["Server"]


FastAPIInstance = TypeVar("FastAPIInstance", bound="FastAPI")


class Server:

    def __init__(self, app: FastAPI):
        self.__app = app
        self._register_routes(app)

    def get_app(self) -> FastAPIInstance:
        return self.__app

    @staticmethod
    def _register_routes(app: FastAPIInstance) -> None:
        __routes__.allocate_routes(app)
