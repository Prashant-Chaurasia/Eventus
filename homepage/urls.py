from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [

    url(r'^$',views.home, name='homepage'),
    url(r'^contactus$',views.contact_new, name='contactus'),

]
