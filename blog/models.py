from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model) :
     author = models.ForeignKey(User , related_name='post_author',on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to='posts/')
     description = models.TextField(max_length=3000)
     created_at = models.DateTimeField(default=timezone.now)
     likes = models.ManyToManyField(User)
     
     