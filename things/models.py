from enum import unique
from unicodedata import name
from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Thing(Model):
    name = models.CharField(max_length=30, blank=False,unique=True)
    description = models.CharField(max_length=120, blank=True, unique=False)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], unique=False)
