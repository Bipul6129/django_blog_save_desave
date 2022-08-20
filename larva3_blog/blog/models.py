from email.policy import default
from django.db import models
from django.utils import timezone
from account.models import Account
from django.urls import reverse

# Create your models here.

class Post_blog(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(default='blog-pics/default.jpg',upload_to='blog-pics')
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('login-home')

class user_blog_manager(models.Manager):
    def get_title(self):
        return self.blog.title 


class User_Blog(models.Model):
    blog=models.ForeignKey(Post_blog,on_delete=models.CASCADE)
    author = models.ForeignKey(Account,on_delete=models.CASCADE,)
    objects=user_blog_manager()
 
    def __str__(self):
        return self.blog.title + str(self.id)
    
    

    