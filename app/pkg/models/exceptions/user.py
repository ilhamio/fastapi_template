from fastapi import status

from app.pkg.models.base import BaseAPIException


class UserAlreadyExist(BaseAPIException):
    status_code = status.HTTP_409_CONFLICT
    message = "User already exist."
