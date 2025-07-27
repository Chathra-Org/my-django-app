# models.py
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()

    def __str__(self):
        return self.username
from django.db import models

# Create your models here.
