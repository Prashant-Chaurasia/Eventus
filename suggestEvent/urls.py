from django.conf.urls import url
from . import views

app_name = "suggest"

urlpatterns = [
    # post views
    url(r'^Suggest$', views.Suggest_Event, name='suggestEvent'),
]