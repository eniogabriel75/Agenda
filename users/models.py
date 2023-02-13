from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    registration = models.CharField(max_length=20)
    password = models.CharField(max_length=64)
    tipo = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.name



