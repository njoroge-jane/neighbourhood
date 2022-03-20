from django.db import models

# Create your models here.

class Neighbour(models.Model):
  home_name = models.CharField()
  location = models.CharField()
  occupants_count = models.IntegerChoices()
  admin = models.ForeignKey(User)

class User(models.Model):
  name = models.CharField()
  id = models.IntegerField()
  neighbour_id = models.ForeignKey(Neighbour)
  email = models.EmailField()



class Business(models.Model):
  business_name = models.CharField()
  user =  models.ForeignKey(User)
  neighbour_id = models.ForeignKey(Neighbour)
  business_email= models.EmailField()


