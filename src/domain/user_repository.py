from abc import ABC, abstractmethod
from typing import Optional

from src.domain.user import User


class UserRepository(ABC):

    @abstractmethod
    def get_by_username(self, username: str) -> Optional[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def update(self, email: str) -> None:
        pass
