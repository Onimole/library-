from distutils.text_file import TextFile
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length= 150)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=50)

    def __str__(self):
        return {"title", "subtitle", "author", "isbn" }