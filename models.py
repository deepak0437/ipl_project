from django.db import models

# Create your models here.
class Ipl(models.Model):
    name = models.CharField(max_length=70)
    team = models.CharField(max_length=70)
    price = models.CharField(max_length=70)
    play = models.CharField(max_length=70)
    role = models.CharField(max_length=70)
    """
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    """