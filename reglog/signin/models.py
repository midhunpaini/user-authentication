from asyncio.windows_events import NULL
from email.policy import default
from tkinter import Widget
from django.db import models

# Create your models here.
class Signup(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
class Signin(models.Model):
    signin = Signup()
    username = signin.username
    password = signin.password
    