from abc import abstractmethod
from model import ValidationResult


class BaseValidator:
    @abstractmethod
    def validate(self, data: str) -> ValidationResult:
        pass
