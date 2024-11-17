from django.db import models
from django.core.validators import *
from fruitipediaApp.fruits.validators import name_only_letter


# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        validators=(
            MinLengthValidator(2),
            MaxLengthValidator(30),
            name_only_letter
        )
    )

    img_url = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    # this is for FK Relationship
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
