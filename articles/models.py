from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default = 'defualt.png', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
    
    def snippet(self):
        return (self.body[:50]+'...')
    
    def get_absolute_url(self):
        return reverse('articles:list')
        