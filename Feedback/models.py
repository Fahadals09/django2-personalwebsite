from django.db import models

# Create your models here.

class Feedback(models.Model) :
    description = models.TextField(max_length=3000)
    name = models.TextField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    personaljob = models.TextField(max_length=100)
