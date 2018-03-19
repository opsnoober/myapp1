from django.db import models

# Create your models here.
class Cal(models.Model):

    cs = models.IntegerField()
    bcs = models.IntegerField()
    result = models.IntegerField()
