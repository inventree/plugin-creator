import keyword
import re

from questionary import Validator, ValidationError


class NotEmptyValidator(Validator):
    """Ensure that the input is not empty."""

    def validate(self, document):
        """Ensure that the input is not empty."""
        if not document.text:
            raise ValidationError(message="Input must not be empty")


class ProjectNameValidator(NotEmptyValidator):
    """Validate the project name."""

    def validate(self, document):
        """Ensure that the project name is valid."""

        super().validate(document)

        project_name = document.text

        if len(project_name) > 50:
            raise ValidationError(message="Must be less than 50 characters long")

        # Must not be a reserved keyword
        if keyword.iskeyword(project_name):
            raise ValidationError(message="Must not be a reserved Python keyword")
        
        pattern = r"^[a-zA-Z_][a-zA-Z0-9 ]*$"

        if not re.match(pattern, project_name):
            raise ValidationError(message=f"Must match pattern: '{pattern}'")
