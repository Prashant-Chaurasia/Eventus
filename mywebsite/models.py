from django.db import models
from django.utils import timezone
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

#Model for Event
class Event(models.Model):
    author = models.ForeignKey('auth.User')
    Event_Name = models.CharField(max_length=200)
    Organized_By = models.TextField()
    Event_Image = models.FileField(null=True, blank=True)
    Short_Description_Of_Event = models.CharField(max_length=300)
    Long_Description_Of_Event = models.TextField()
    Categories = models.TextField()
    Event_Start_Date = models.DateField()
    Event_Last_Date = models.DateField()
    Last_Date_For_Apply = models.DateField(null=True,blank=True)
    Rulebook_Of_Event = models.FileField(null=True, blank=True)
    Apply_Link_Of_Event = models.TextField()
    Venue_Of_Event = models.TextField()
    Terms_and_Condtions_Of_Event = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Event_Name

class Comment(models.Model):
    event = models.ForeignKey('mywebsite.Event', related_name='comments')
    author = models.CharField(max_length=300)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


#Model for Exhibition
class Exhibition(models.Model):
    author = models.ForeignKey('auth.user')
    Exhibition_Name = models.CharField(max_length=200)
    Organized_by = models.CharField(max_length=300)
    Sponsered_by = models.TextField()
    Exhibition_Image = models.FileField(null=True, blank=True)
    Exhibition_Venue = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.Exhibition_Name


