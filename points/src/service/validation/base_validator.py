from abc import abstractmethod

from points.src.model.validation_result import ValidationResult


class BaseValidator:
    @abstractmethod
    def validate(self, data: str) -> ValidationResult:
        pass
