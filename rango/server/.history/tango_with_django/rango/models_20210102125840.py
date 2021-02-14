from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.template.defaultfilters import slugify

# Create your models here.
class User(AbstractUser):
    pass

    def __str__(self):
        return f'{self.username}'


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
# Create your models here.
