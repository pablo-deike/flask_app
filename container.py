from typing import Any
from flask_sqlalchemy import SQLAlchemy

from src.infrastructure.db_user_repository import DbUserRepository
from src.infrastructure.verification_controller import VerificationController


class Container:
    def __init__(self):
        self._services = {}
        self._singletons = {}

    def register(self, key: str, provider: Any, singleton: bool = False):
        self._services[key] = (provider, singleton)

    def resolve(self, key: str):
        provider, singleton = self._services.get(key, (None, False))
        if provider:
            if singleton:
                if key not in self._singletons:
                    self._singletons[key] = provider(self)
                return self._singletons[key]
            return provider(self)
        raise KeyError(f"Service not found: {key}")


container = Container()
container.register("db_instance", lambda c: SQLAlchemy())
db = container.resolve("db_instance")
container.register("user_repository", lambda c: DbUserRepository(db))
container.register(
    "verification_controller",
    lambda c: VerificationController(c.resolve("user_repository")),
)
verification_controller = container.resolve("verification_controller")
