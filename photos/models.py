from django.db import models

# Create your models here.

class photos(models.Model):
    path = models.ImageField(blank=False,null=False,)
