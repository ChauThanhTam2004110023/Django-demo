from django.shortcuts import render
from django.http import HttpResponse
from .views import *
from django.views import View

# Create your views here.
def index(request):
    return HttpResponse('e-course app.')


def welcome(request, year):
    return HttpResponse("HELLO " + str(year))


def welcome2(request, year):
    return HttpResponse("Hello " + str(year))


class TestView(View):
    def get(self, request, year):
        return HttpResponse("TESTING " + str(year))

    def post(self, request):
        pass
