from typing import override
from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.


class Book(models.Model):
    title: CharField = models.CharField(max_length=200)
    author: CharField = models.CharField(max_length=100)
    published_date: DateField = models.DateField()
    genre: CharField = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title.__str__()
