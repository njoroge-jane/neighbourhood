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


class Neighbour(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    neighbourhood_id = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE)
    email = models.EmailField()


class Business(models.Model):
    business_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourhood_id = models.ForeignKey(
        Neighbourhood, on_delete=models.CASCADE, null=True)
    business_email = models.EmailField()
