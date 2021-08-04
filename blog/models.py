from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Post(models.Model) :
     author = models.ForeignKey(User , related_name='post_author',on_delete=models.CASCADE)
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to='posts/')
     content = models.TextField(max_length=3000)
     created_at = models.DateTimeField(default=timezone.now)
     likes = models.ManyToManyField(User)
     tags = TaggableManager()

     
     def __str__(self):
        return  self.title 

     