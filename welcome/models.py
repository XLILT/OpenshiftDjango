from django.db import models

# Create your models here.

class message(models.Model):
    username = models.CharField(max_length=20)
    password = modelsCharField(max_length=15)
