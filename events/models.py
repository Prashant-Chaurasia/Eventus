from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class PostedManager(models.Manager):
    def get_queryset(self):
        return super(PostedManager,self).get_queryset()


class Events(models.Model):
    objects = models.Manager()
    posted = PostedManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='postdate')
    author = models.ForeignKey(User,related_name='event_posts')
    postdate = models.DateTimeField(default=timezone.now)
    cover_image = models.FileField(null=True, blank=True)
    short_description = models.CharField(max_length=300)
    long_description = models.TextField(null=True,blank=True)
    categories = models.TextField()
    start_date = models.DateField()
    last_date = models.DateField()
    last_date_to_apply = models.DateField(null=True, blank=True)
    rulebook = models.FileField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
    venue = models.TextField()
    terms_and_conditions = models.FileField(null=True,blank=True)
    college = models.CharField(max_length=500,default="null")
    inter_event = models.BooleanField(default=False)
    city = models.CharField(max_length=150,default="null")

    def get_absolute_url(self):
        return reverse('events:event_detail',
                       args=[self.postdate.year,
                             self.postdate.strftime('%m'),
                             self.postdate.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-postdate',)

    def __str__(self):
        return self.title