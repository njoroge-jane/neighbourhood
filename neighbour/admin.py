from django.contrib import admin
from .models import Neighbour,Neighbourhood,Business

# Register your models here.
admin.site.register(Neighbour)
admin.site.register(Neighbourhood)
admin.site.register(Business)