from typing import Any

from src.domain.user_builder import UserBuilder
from src.infrastructure.register_controller import RegisterController
from src.infrastructure.db_user_repository import DbUserRepository
from src.infrastructure.auth_controller import AuthController
from init_db import db, bcrypt


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
container.register("user_repository", lambda c: DbUserRepository(db))
container.register("user_builder", lambda c: UserBuilder())
container.register(
    "auth_controller",
    lambda c: AuthController(user_repository=c.resolve("user_repository")),
)
container.register(
    "register_controller",
    lambda c: RegisterController(
        user_repository=c.resolve("user_repository"),
        user_builder=c.resolve("user_builder"),
    ),
)
user_repository: DbUserRepository = container.resolve("user_repository")
auth_controller: AuthController = container.resolve("auth_controller")
register_controller: RegisterController = container.resolve("register_controller")
