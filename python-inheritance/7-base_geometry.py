#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """Represents a base geometry object."""
    def area(self):
        raise Exception("area() is not implemented")
        def integer_validator(self, name, value):
             """
        Validates an integer value.

        Args:
            name (str): The name associated with the value.
            value (int): The value to be validated.

        Raises:
            ValueError: If the value is not an integer.

        Example:
            validator = Validator()
            validator.integer_validator("age", 25)  # Valid
            validator.integer_validator("score", "100")  # Raises ValueError
        """
        if not isinstance(value, int):
             raise ValueError(f"{name} must be an integer.")
         if value <= 0:
            raise ValueError(f"{name} must be greater than 0.")
