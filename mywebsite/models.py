from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


# Model for Registration

class College(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=50, blank=True)
    mail_id = models.CharField(max_length=70)


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, primary_key=True)
    email_id = models.CharField(max_length=100)
    password = models.CharField(max_length=5000)
    clg_code = models.ForeignKey(College, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=5000)
    roll_No = models.CharField(max_length=100)
    clg_code = models.ForeignKey(College, on_delete=models.CASCADE)
