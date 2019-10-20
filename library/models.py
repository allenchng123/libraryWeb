from django.db import models
import datetime
from django.utils import timezone

# -------------------------------------------------------------
class User(models.Model):
    username = models.CharField(max_length=50, null=False,blank=False)
    password = models.CharField(max_length=50, null=False,blank=False)
    a = models.CharField(max_length=50, null=True,blank=True)

# -------------------------------------------------------------
class Book(models.Model):
    img = models.ImageField(upload_to="pic",blank=True,null=True)
    title = models.CharField(max_length=50, null=False)
    category = models.CharField(max_length=50,blank=True,null=True)
    author = models.CharField(max_length=50,blank=True,null=True)
    publisher = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    dateOfBorrow = models.DateTimeField(blank=True,null=True)
    dateOfReturn = models.DateTimeField(blank=True,null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.title

    