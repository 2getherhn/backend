"""2gether URL Configuration

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

from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required
import app.views as views


admin.autodiscover()
admin.site.login = login_required(admin.site.login)
admin.site.site_header = '2Gether we help'

urlpatterns = [
    # home views
    path('', views.home_view, name="home"),
    path('shelter', views.save_shelter, name="shelter-form"),
    path('login', views.login_view, name="login"),
]
