from django.db import models
from django.core import serializers

class Genre(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return self.name