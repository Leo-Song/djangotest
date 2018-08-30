from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

def index(request):
    return  HttpResponse(u'看什么看，没看过帅哥吗？')

def index2(request):
    return  render(request, 'home.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def redirect(request, a, b):
    return HttpResponseRedirect(reverse_lazy('add2', args=(a,b)))