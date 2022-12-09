from starlette import status

from app.pkg.models.base import BaseAPIException

__all__ = ["EmptyABI", "NotEnoughMoney", "CantPayForGas"]


class EmptyABI(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Empty abi."


class NotEnoughMoney(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Not enough coin money."


class CantPayForGas(BaseAPIException):
    status_code = status.HTTP_400_BAD_REQUEST
    message = "Can't pay fee for gas."
