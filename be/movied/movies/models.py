from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


BASE_URL = 'http://127.0.0.1:8020'

class Actor(models.Model):
    name = models.CharField(max_length=250)
    birth_date = models.DateField()
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    
    def __str__(self):
        return self.name

    def get_age(self):
        age = datetime.date.today() - self.birth_date

    def image_url(self):
        if self.image:
            return BASE_URL + self.image.url
        return ''


class Movies(models.Model):
    title = models.CharField(max_length=250)
    actor = models.ManyToManyField(Actor)
    genre = models.CharField(max_length=250, null=True, blank=True, default=None)
    release_year = models.IntegerField(blank=True, null=True, default=None)
    slug = models.SlugField(blank=True, null=True)
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(10.0)])
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_url(self):
        if self.image:
            return BASE_URL + self.image.url
        return ''
