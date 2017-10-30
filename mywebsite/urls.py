from django.conf.urls import url
from . import views
from mywebsite import views as core_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^firstpage/$', views.firstpage, name='firstpage'),
    url(r'^accounts/signup/$', core_views.signup, name='signup'),
    url(r'^accounts/signup/company/$', core_views.signupForOrganizer, name='signupForOrganizer'),
    url(r'^events/$', views.events_list, name='events_list'),
    url(r'^events/post/new/$', views.events_new, name='events_new'),
    #url(r'^secondpage/post/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^events/post/(?P<pk>\d+)/$', views.events_detail, name='events_detail'),

]