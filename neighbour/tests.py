from django.test import TestCase
from .models import Neighbour,Neighbourhood,Business
from django.contrib.auth.models import User
# Create your tests here.

class NeighbourhoodTest(TestCase):
  def setUp(self):
    self.new_neighbourhood=Neighbourhood(name='Don',location='Gate c',admin=User)
    

  def test_instance(self):
    self.assertTrue(isinstance(self.new_admin,User))
 
  def test_save_neighbourhood(self):
    self.new_neighbourhood.save()
    self.assertTrue(len(Neighbourhood.objects.all())>0)

  def test_delete_neighbourhood(self):
    self.new_neighbourhood.save()
    self.target_neighbourhood=Neighbourhood.objects.filter(name='Don').first()

    Neighbourhood.delete_neighbourhood()
    self.assertTrue(len(Neighbourhood.objects.all())==0)

class BusinessTest(TestCase):
  '''
  Business test class to test the the methods for business model
  '''
  def setUp(self):
    self.new_neighbourhood=Neighbourhood(name='Don',location='Gate c',admin=Neighbour.name)
    self.new_user=User(first_name='Jane',last_name='Njoroge',username='janey',email="jwnjoroge4@gmail.com",password='access')
    self.new_profile=Neighbour(name='Janey',national_id='0000000',user=self.new_user,neighbourhood=self.new_neighbourhood,email='jwnjoroge4@gmail.com')
    self.new_business=Business(name='Eggs N Bake',profile=self.new_profile,neighbourhood=self.new_neighbourhood,email='eggs@gmail.com')
  
  def test_create_business(self):
    self.new_neighbourhood.save()
    self.new_user.save()
    self.new_profile.save()
    self.new_business.save()
    self.assertTrue(len(Business.objects.all())>0)

  def delete_business(self):
    self.new_user.save()
    self.new_profile.save()
    self.new_business.save()
    self.business=Business.objects.all()
    self.business.delete_business()
    self.assertTrue(len(Business.objects.all())==0)
