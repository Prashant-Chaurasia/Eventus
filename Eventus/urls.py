"""Eventus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from account.regbackend2 import StudentRegistrationView
from account import views
from userProfile.views import edit_user

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/register/$', StudentRegistrationView.as_view(), name='registration_register'),
    url(r'^home/',views.home, name = 'home'),
    url(r'',include('events.urls',namespace='events',app_name='events')),
    url(r'',include('college.urls',namespace='college',app_name='college')),
    url(r'',include('club.urls',namespace='club',app_name='club')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^',include('homepage.urls')),
    url(r'^Update/', edit_user, name='update'),
    url(r'^', include('suggestEvent.urls'))
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)