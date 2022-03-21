from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from .forms import UploadImageForm,ProfileForm
from .models import Business,Neighbour,Neighbourhood

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  posts = Business.objects.all()


  return render(request,'index.html', {"posts": posts})
