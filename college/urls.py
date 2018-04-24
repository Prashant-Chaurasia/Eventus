from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^colleges/$', views.College_list, name='college_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/'r'(?P<college>[-\w]+)/$', views.College_detail,name='college_detail'),
    url(r'^colleges/new/$', views.Add_College, name='add_college'),
]
