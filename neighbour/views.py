from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, UploadForm
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

def search_results(request):

    if 'users' in request.GET and request.GET["users"]:
        search_term = request.GET.get("users")
        searched = Business.search_by_user(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched": searched})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
        return redirect('index')

    else:
        form = UploadForm()
    return render(request, 'upload.html', {"form": form})
  