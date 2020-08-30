"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='/login')),
    url(r'^lycee/',include('lycee.urls')),
    url(r'^register/$', views.signup, name='signup'),
    url(r'', include('django.contrib.auth.urls')),
]

handler404 = 'mysite.views.error_404'
handler500 = 'mysite.views.error_500'
handler403 = 'mysite.views.error_403'
handler400 = 'mysite.views.error_400'