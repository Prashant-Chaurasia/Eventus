from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class CollegeCode(models.Model):

    Code = models.CharField(max_length=50,primary_key= True)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Faculty(models.Model):

    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User)
    Code = models.ForeignKey(CollegeCode, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class Students(models.Model):
    Name = models.CharField(max_length=50)
    user = models.OneToOneField(User)
    RollNo = models.CharField(max_length=50)
    Code = models.ForeignKey(CollegeCode, on_delete=models.CASCADE)
    Course = models.CharField(max_length=50, blank=True)
    Batch = models.CharField(max_length=50, blank=True)
    Year = models.CharField(max_length=50, blank=True)
    About = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.Name

'''
def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = Students(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)
'''