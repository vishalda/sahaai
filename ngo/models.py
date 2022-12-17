from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

class Organization(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15,blank = True,null=True)
    description = models.TextField(blank=True,null=True)
    location=models.TextField(blank=True,null=True)
    links=models.TextField(blank=True,null=True)
    logo=models.ImageField(upload_to="images")
    qrCode=models.ImageField(upload_to="images")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
