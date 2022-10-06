from enum import unique
from unicodedata import name
from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Thing(Model):
    name = models.TextField(max_length=30)
    description = models.TextField()
    quantity = models.IntegerField()
