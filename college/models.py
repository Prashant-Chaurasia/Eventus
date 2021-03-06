from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10

CITY_CHOICES = (
        ('GN', 'Gandhinagar'),
        ('ADI', 'Ahmedabad'),
    )
class CollegeManager(models.Manager):
    def get_queryset(self):
        return super(CollegeManager,self).get_queryset()

def college_logo_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}/{2}/{3}'.format(instance.author.id,instance.name,'logo',filename)

class College(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

    objects = models.Manager()
    posted = CollegeManager()
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='postdate')
    author = models.ForeignKey(User,related_name='college_posts')
    postdate = models.DateTimeField(default=timezone.now)
    logo = models.FileField(null=True, blank=True,upload_to=college_logo_path)
    scc_mail_id = models.EmailField()
    description = models.TextField(max_length=500,null=True,blank=True)
    website = models.TextField(null=True, blank=True)
    address = models.TextField(validators=[alphanumeric])
    city = models.CharField(max_length=60 ,choices=CITY_CHOICES,default='Gandhinagar')

    def get_absolute_url(self):
        return reverse('college:college_detail',
                       args=[self.postdate.year,
                             self.postdate.strftime('%m'),
                             self.slug,])

    class Meta:
        ordering = ('-postdate',)

    def __str__(self):
        return self.name

