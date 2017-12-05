from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your models here.

class ClubManager(models.Manager):
    def get_queryset(self):
        return super(ClubManager,self).get_queryset()

def club_logo_path(instance, filename):
    return 'user_{0}/{1}/{2}/{3}/{4}'.format(instance.author.id,instance.name,'club','logo',filename)

class Club(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    users = User.objects.all()
    objects = models.Manager()
    posted = ClubManager()
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique_for_date='postdate')
    author = models.ForeignKey(User,related_name='clubs')
    postdate = models.DateTimeField(default=timezone.now)
    club_image = models.FileField(null=True, blank=True,upload_to=club_logo_path)
    description = models.TextField(max_length=500,null=True,blank=True)
    website = models.CharField(max_length=200,null=True, blank=True)
    secretary = models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('club:club_details',
                       args=[self.postdate.year,
                             self.postdate.strftime('%m'),
                             self.postdate.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-postdate',)

    def __str__(self):
        return self.name