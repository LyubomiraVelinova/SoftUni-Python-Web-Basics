from django.db import models


# Create your models here.

class Task(models.Model):
    # varchar
    title = models.CharField(max_length=30, null=False)
    # text
    description = models.TextField()
    # int
    priority = models.IntegerField(default=1)
