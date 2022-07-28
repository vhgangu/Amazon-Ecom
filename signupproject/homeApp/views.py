from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from .forms import SignupForm 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request):
    return render(request, 'home.html')

def registerfun(request):
    if  request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Resgistered Successfully !!')
            fm.save()
            
    else:
        fm = SignupForm()
    return render(request, 'register.html', {'form':fm})

def login_to(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upwd = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/index/')
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form':fm})

def index(request):
    return render(request, 'index.html')