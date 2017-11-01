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
    url(r'^events/post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^events/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^events/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^exhibition/$', views.exhibitions_list, name='exhibitions_list'),
    url(r'^exhibitions/post/new/$', views.exhibitions_new, name='exhibitions_new'),
    url(r'^exhibitions/post/(?P<pk>\d+)/$', views.exhibitions_detail, name='exhibitions_detail'),
]