from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Business,Neighbour,Neighbourhood

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
  posts = Business.objects.all()


  return render(request,'index.html', {"posts": posts})

def profile(request):
  current_user = request.user
  neighbour = Neighbour.objects.filter(name = current_user).first()
  if request.method == 'POST':

    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
          profile = form.save(commit=False)
          profile.user = current_user
          profile.save()

  else:
        form = ProfileForm()        
  return render(request, 'profile.html',{"form":form,"neighbour":neighbour})
