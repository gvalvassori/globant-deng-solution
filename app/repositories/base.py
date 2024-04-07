"""
The idea of the BaseRepository is simply to abstract the CRUD operations,
thus allowing to respect the same flow for all other repositories.

Q: Why not use the ABC module?
A: Because there would be many decorators and the messages they return are not so explicit.
"""

import os
from functools import wraps
from typing import Any, Callable, cast, no_type_check

from schemas.types import Model, ModelType
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session


# region Decorators
@no_type_check
def model_required(method: classmethod) -> Any:
    """Check if model is assigned in the inheritance"""

    @wraps(method)
    def wrapper(self=None, *args: Any, **kwargs: Any) -> Any:
        if self is None:
            raise TypeError(f"The '{method.__name__}' is not a class method")
        if not isinstance(self.model, type(Model)):
            raise ValueError(f"The '{self.__name__}' unassigned model's instance")
        return method(self, *args, **kwargs)

    return wrapper


@no_type_check
def only_tests(method_or_func: classmethod | staticmethod | Callable[..., Any]) -> Any:
    """Limits its use, it can only be used in test environments."""

    @wraps(method_or_func)
    def wrapper(self=None, *args: Any, **kwargs: Any) -> Any:
        if str(os.environ.get("PYTEST_RUNNING")).lower() != "true":
            raise NotImplementedError(
                "You cannot use this method outside test environment"
            )
        if self:
            return method_or_func(self, *args, **kwargs)
        return method_or_func(*args, **kwargs)

    return wrapper


class ModelRepository:
    model: Any = cast(Model, None)

    def __init__(self, session: Session):
        self.session = session

    @model_required
    def get_all(self) -> list[ModelType]:
        """
        Gets all records from the table.

        :return: a list of models, example = ["<ModelType 1>", "<ModelType 2>", ...]
        """
        return self.session.query(self.model).all()  # noqa

    @model_required
    def bulk_insert(self, list_instances: list[ModelType]) -> bool:
        """
        Inserts a list of instances in the database.

        :param list_instances: A list of instances to be inserted
        :returns: True if the operation is completed, False if an error generated.
        """
        try:
            self.session.bulk_save_objects(list_instances)
            self.session.commit()
            return f"A total of {len(list_instances)} instances were inserted in the database."
        except SQLAlchemyError as e:
            return f"An error occurred while inserting the instances: {e}"
