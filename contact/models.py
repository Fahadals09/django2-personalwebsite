from django.db import models

# Create your models here.
class contact(models.Model) :
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    message= models.TextField(max_length=3000)

    #return - name
    def __str__(self):
        return  self.name

   