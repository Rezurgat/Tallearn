from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog_articles/')
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return f'{self.title}  {self.author} - ({self.create_at})'

    class Meta:
        ordering = ['create_at']


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)
    format = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return f'{self.title}  {self.author} - ({self.create_at})'

    class Meta:
        ordering = ['create_at']


class Comment(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, null=True, blank=True)
    comment = models.TextField(max_length=256)
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstname}  {self.lastname} - ({self.email})'

    class Meta:
        ordering = ['create_at']


