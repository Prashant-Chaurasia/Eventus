from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^events/$', views.events_list, name='events_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'r'(?P<event>[-\w]+)/$', views.event_detail,name='event_detail'),
    url(r'^events/new/$', views.create_event, name='create_event'),
]
