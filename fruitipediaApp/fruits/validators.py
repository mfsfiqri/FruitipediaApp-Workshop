from django.core.exceptions import ValidationError

def name_only_letter(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
