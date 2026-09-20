from django.core.exceptions import ValidationError



def name_validator(value):
    for char in value:
        if not (char.isalpha() or char == "'"):
            raise ValidationError("First name can only contain letters and apostrophes.")


def genre_name_validator(value):
    for char in value:
        if not (char.isalpha() or char == "'" or char == " "):
            raise ValidationError("Genre name can only contain letters, apostrophes, and spaces.")
