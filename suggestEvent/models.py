from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from account.models import CollegeCode
# Create your models here.


class Suggest(models.Model):

    author = models.OneToOneField(User)
    Name = models.CharField(max_length=100)
    Details = models.CharField(max_length=500)
    upvotes = models.IntegerField(blank=True, default=0)
    downvotes = models.IntegerField(blank=True, default=0)
    postdate = models.DateTimeField(default=timezone.now)
    Code = models.ForeignKey(CollegeCode, on_delete=models.CASCADE)
