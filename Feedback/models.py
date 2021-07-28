from django.db import models

# Create your models here.

class Feedback(models.Model) :
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    personaljob = models.CharField(max_length=100)
    description = models.TextField(max_length=3000)


    def __str__(self):
        return  self.name 

