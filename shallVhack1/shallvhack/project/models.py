from django.db import models

# Create your models here.
class shallvhack(models.Model):
    title = models.CharField(max_length=90)
    desc = models.TextField()