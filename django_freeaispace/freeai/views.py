from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
# Create your views here.


def index(request): 
    return render(request,'freeai/index-2.html')