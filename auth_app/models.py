from django.db import models


# Create your models here.

class ImageProcessing(models.Model):
    unique_code = models.CharField(max_length=20, unique=True)
    image = models.ImageField()
