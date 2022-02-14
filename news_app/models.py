from pydoc import describe
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    date_field = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
