from django.db import models

# Create your models here.
class contact(models.Model) :
    name= models.CharField(max_length=100)
    email= models.TextField(max_length=300)
    message= models.TextField(max_length=3000)

   