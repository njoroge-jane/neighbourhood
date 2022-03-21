from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path

from . import views

urlpatterns=[
path('', views.index, name='index'),
path('profile/', views.profile, name='profile'),
path('search', views.search_results, name='search_results'),
]
