"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from tastypie.api import Api
from api.resources import SalaResource, UserResource, RoomResource, PeriodResource

v1_api = Api(api_name='v1')
v1_api.register(SalaResource())
v1_api.register(UserResource())
v1_api.register(RoomResource())
v1_api.register(PeriodResource())



urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^api/', include(v1_api.urls)),
]
