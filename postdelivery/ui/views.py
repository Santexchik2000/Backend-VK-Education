from django.contrib.auth import logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request): 
    return render(request, 'login.html')

def logout_view(request):
    logout(request);
    return HttpResponseRedirect('/')
    
