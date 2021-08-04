from django.db import models

# Create your models here.
class About(models.Model) :
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    description = models.TextField(max_length=3000)

    def __str__(self):
        return  self.title 