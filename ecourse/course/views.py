from django.shortcuts import render
from django.http import HttpResponse
from .views import *

# Create your views here.
def index(request):
    return HttpResponse('e-course app.')