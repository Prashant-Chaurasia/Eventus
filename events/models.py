from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.

class PostedManager(models.Manager):
    def get_queryset(self):
        return super(PostedManager,self).get_queryset()

def event_cover_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.author.id,'cover',filename)

def event_rulebook_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}'.format(instance.author.id,'rulebook',filename)

class Events(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    objects = models.Manager()
    posted = PostedManager()
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='postdate')
    author = models.ForeignKey(User,related_name='event_posts')
    postdate = models.DateTimeField(default=timezone.now)
    cover_image = models.FileField(null=True, blank=True,upload_to=event_cover_path)
    description = models.TextField(null=True,blank=True)
    categories = models.TextField()
    start_date = models.DateField()
    last_date = models.DateField()
    last_date_to_apply = models.DateField(null=True, blank=True)
    rulebook = models.FileField(null=True, blank=True,upload_to=event_rulebook_path)
    website = models.CharField(max_length=250,null=True, blank=True)
    facebook_link = models.CharField(max_length=250,null=True,blank=True)
    venue = models.CharField(validators=[alphanumeric],max_length=500)
    college = models.CharField(validators=[alphanumeric],max_length=250,null=True)
    inter_event = models.BooleanField(default=False)
    register = models.BooleanField(default=False)
    no_of_tickets = models.IntegerField(default=0)


    def get_absolute_url(self):
        return reverse('events:event_detail',
                       args=[self.postdate.strftime('%Y'),
                             self.postdate.strftime('%m'),
                             self.postdate.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-postdate',)

    def __str__(self):
        return self.title