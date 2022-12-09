"""All enum inside models must be inherited by `BaseEnum`"""
from enum import Enum
from typing import Any, Dict

import pydantic

__all__ = ["BaseEnum"]


class BaseModel(pydantic.BaseModel):
    def to_dict(
        self,
        show_secrets: bool = False,
        values: Dict[Any, Any] = None,
        bytes_to_string: bool = False,
        by_alias: bool = True,
        **kwargs,
    ) -> Dict[Any, Any]:
        """Make transfer model to Dict object.

        Args:
            by_alias: Whether field aliases should be used as keys in the
                returned dictionary
                Default: ``True``.
            show_secrets: Shows secret in dict object if True.
                Default: ``False``.
            values: Using an object to write to a Dict object.
                Default: ``None``.
            bytes_to_string: Using an object to convert byte objects to string.
                Default: ``False``.
        Keyword Args:
            Optional arguments to be passed to the Dict object.

        Returns: Dict object with reveal password filed.
        """
        values = (
            self.dict(by_alias=by_alias, **kwargs).items()
            if not values
            else values.items()
        )
        r = {}
        for k, v in values:
            if isinstance(v, pydantic.SecretBytes):
                v = v.get_secret_value() if show_secrets else str(v)
                if bytes_to_string:
                    v = v.decode("utf-8")
            elif isinstance(v, pydantic.SecretStr):
                v = v.get_secret_value() if show_secrets else str(v)
            elif isinstance(v, Dict):
                v = self.to_dict(show_secrets=show_secrets, values=v)
            r[k] = v
        return r

    def delete_attribute(self, attr: str) -> pydantic.BaseModel:
        """Delete `attr` field from model.

        Args:
            attr: str value, implements name of field.

        Returns: self object.
        """
        delattr(self, attr)
        return self

    class Config:

        #: Boolean: Use enum values.
        use_enum_values = True
        #: Dict[object, Callable]: custom json encoder.
        json_encoders = {
            pydantic.SecretStr: lambda v: v.get_secret_value() if v else None,
            pydantic.SecretBytes: lambda v: v.get_secret_value() if v else None,
            bytes: lambda v: v.decode() if v else None,
        }


class BaseEnum(Enum):
    """Base ENUM model."""

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return str(self.value)
