from hashlib import new
from site import USER_SITE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Neighbourhood(models.Model):
    DONHOLM = 'DON'
    PIPELINE = 'PIP'
    BURUBURU = 'BUR'
    FEDHA = 'DHA'
    EMBAKASI = 'EMB'
    HOME_NAME = [
        (DONHOLM, 'Donholm'),
        (PIPELINE, 'Pipeline'),
        (BURUBURU, 'Buruburu'),
        (FEDHA, 'Fedha'),
        (EMBAKASI, 'Embakasi'),
    ]
    home_name = models.CharField(
        max_length=3, choices=HOME_NAME, default=DONHOLM,)
    location = models.CharField(max_length=30)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.home_name  

    def save_neighbourhood(self):
        self.save() 

    def delete_neighbourhood(self):
        self.delete() 

    def update_neighbourhood(self) :
        self.objects.all().update()

    def update_occupants_count(self):
        User.objects.filter(id).update(occupants_count=False)
                       

class Neighbour(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    neighbourhood_id = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.name  

    def save_neighbour(self):
        self.save() 

    def delete_neighbour(self):
        self.delete() 


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood_id = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, null=True)
    business_email = models.EmailField()

    def __str__(self):
        return self.business_name 

    def save_business(self):
        self.save() 

    def delete_business(self):
        self.delete()     

    @classmethod
    def search_business(cls,search_term):
        business =  Business.objects.filter(business_name__icontains=search_term)
        return business 

    def update_business(self) :
        self.objects.all().update()   

               