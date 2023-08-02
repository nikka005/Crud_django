from django.db import models

# Create your models here.

class St(models.Model):
    name = models.CharField('Name', max_length=250)
    email = models.EmailField()

    def __str__(self):
        return St.name