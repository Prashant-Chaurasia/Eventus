from django.conf.urls import url
from . import views
from account import views as core_views
import django.contrib.auth.views as auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^firstpage/$', views.firstpage, name='firstpage'),
    url(r'^accounts/signup/$', core_views.signup, name='signup'),
    url(r'^accounts/signup/company/$', core_views.signupForOrganizer, name='signupForOrganizer'),
    url(r'^events/$', views.events_list, name='events_list'),
    url(r'^events/post/new/$', views.events_new, name='events_new'),
    #url(r'^secondpage/post/(?P<pk>\d+)/edit/$', views.event_edit, name='event_edit'),
    url(r'^events/post/(?P<pk>\d+)/$', views.events_detail, name='events_detail'),
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^accounts/profile/$', core_views.view_profile, name='view_profile'),
    url(r'^account_activation_sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activate, name='activate'),
    url(r'^activateForCompany/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        core_views.activateForOrganizer, name='activateForCompany'),


]