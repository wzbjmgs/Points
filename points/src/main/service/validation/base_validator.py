from abc import abstractmethod

from points.src.main.model.validation_result import ValidationResult


class BaseValidator:
    @abstractmethod
    def validate(self, data: str) -> ValidationResult:
        pass
