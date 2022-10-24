from django.db import models
from django.urls import reverse

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=100);
    type = models.CharField(max_length=100);
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('language_detail', kwargs={'pk': self.id})

class Employee(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    years = models.IntegerField()
    languages = models.ManyToManyField(Language)
    def __str__(self):
        return self.name



