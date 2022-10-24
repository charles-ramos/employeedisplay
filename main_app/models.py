from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    years = models.IntegerField()
    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100);
    type = models.CharField(max_length=100);

