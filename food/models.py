

# Create your models here.
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    calories = models.IntegerField(default=0)
    carbohydrates = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)