from django.conf.urls import url
from . import views
from mywebsite import views as core_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^firstpage/$', views.firstpage, name='firstpage'),
    url(r'^accounts/signup/$', core_views.signup, name='signup'),
    url(r'^accounts/signup/company/$', core_views.signupForOrganizer, name='signupForOrganizer'),

]