# api/resources.py

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.conf.urls import url
from tastypie.utils import trailing_slash
from api.models import Sala, User, Room, Period

class SalaResource(ModelResource):
  class Meta:
    queryset = Sala.objects.all()
    resource_name = 'sala'

class RoomResource(ModelResource):
  class Meta:
    queryset = Room.objects.all()
    resource_name = 'room'
    authorization = Authorization()
    fields = ['name', 'description']

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'

class PeriodResource(ModelResource):
  class Meta:
    queryset = Period.objects.all()
    authorization = Authorization()
    resource_name = 'period'