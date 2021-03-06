from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        return f'{self.username}'


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(null=True, blank=True, max_length=150)
    url = models.URLField(null=True, blank=True, max_length=150)
    views = models.IntegerField(default=0)

    class  Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

