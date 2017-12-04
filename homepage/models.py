from django.db import models

# Create your models here.

#Model for ContactUs
class Contact(models.Model):
    Name = models.CharField(max_length=200, help_text='Name')
    Email = models.CharField(max_length=200, help_text='Email')
    Comment = models.TextField(max_length=1000, help_text='Comment')
