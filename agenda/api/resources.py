# api/resources.py

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from django.conf.urls import url
from tastypie.utils import trailing_slash
from api.models import Sala, User, Room, Period
import tastypie

class SalaResource(ModelResource):
  class Meta:
    queryset = Sala.objects.all()
    resource_name = 'sala'

class RoomResource(ModelResource):
  class Meta:
    queryset = Room.objects.all()
    authorization = Authorization()
    fields = ['name', 'description']
    resource_name = 'room'

class UserResource(ModelResource):
  period = tastypie.fields.ToManyField('PeriodResource', 'period', null=True, full=True)
  class Meta:
    queryset = User.objects.all()
    authorization = Authorization()
    # fields = ['name', 'email']
    resource_name = 'user'

class PeriodResource(ModelResource):
  user = tastypie.fields.ForeignKey(UserResource, 'user', null=True, full=True)
  class Meta:
    # queryset = Period.objects.all()
    queryset = Period.objects.select_related('user')
    print(str(queryset.query))
    authorization = Authorization()
    resource_name = 'period'