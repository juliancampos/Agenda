from django.db import models

# Sala
class Sala(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s - %s' % (self.name, self.description)



# Room
class Room(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s - %s' % (self.name, self.description)



# User
class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(default='')
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s' % (self.name)



# Period
class Period(models.Model):
  start_date = models.DateField()
  start_at = models.TimeField()
  finish_at = models.TimeField()
  user = models.ForeignKey('User', related_name='user', on_delete=models.CASCADE, null=True)
  room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s %s %s %s %s' % (self.start_date, self.start_at, self.finish_at, self.user, self.room)
