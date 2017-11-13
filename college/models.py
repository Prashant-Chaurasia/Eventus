from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class PostedManager(models.Manager):
    def get_queryset(self):
        return super(PostedManager,self).get_queryset()

def college_logo_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}/{3}'.format(instance.author.id,instance.name,'logo',filename)

class College(models.Model):
    CITY_CHOICES = (
        ('GN', 'Gandhinagar'),
        ('ADI', 'Ahmedabad'),
    )

    objects = models.Manager()
    posted = PostedManager()
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='postdate')
    author = models.ForeignKey(User,related_name='college_posts')
    postdate = models.DateTimeField(default=timezone.now)
    logo = models.FileField(null=True, blank=True,upload_to=college_logo_path)
    scc_mail_id = models.EmailField()
    description = models.TextField(null=True,blank=True)
    website = models.TextField(null=True, blank=True)
    address = models.TextField()
    city = models.CharField(max_length=150, default="Gandhinagar", choices=CITY_CHOICES)

    def get_absolute_url(self):
        return reverse('college:college_details',
                       args=[self.postdate.year,
                             self.postdate.strftime('%m'),
                             self.postdate.strftime('%d'),
                             self.slug])

    class Meta:
        ordering = ('-postdate',)

    def __str__(self):
        return self.name