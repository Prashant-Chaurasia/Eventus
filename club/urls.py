from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^clubs/$', views.View_And_Add_Club, name='add_club'),
]