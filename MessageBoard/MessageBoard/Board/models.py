from django.db import models
class blog(models.Model):
    title = models.CharField(max_length = 128)
    contents = models.TextField()
# Create your models here.

