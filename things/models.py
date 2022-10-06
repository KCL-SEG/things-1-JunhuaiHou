from enum import unique
from unicodedata import name
from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Thing(Model):
    name = models.TextField(unique = True, max_length=30, blank = False)
    description = models.TextField(max_length=120)
    quantity = models.IntegerField()
