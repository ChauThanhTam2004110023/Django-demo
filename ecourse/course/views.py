from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .views import *
from django.views import View
# django-rest
from rest_framework import viewsets, permissions
from .models import Course
from .serializers import CourseSerializer

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

    def post(self, request, year):
        return HttpResponse('HELLO ', str(year))
    


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # list {GET} --> xem danh sách khóa học
    # {POST} --> them khóa học
    # detail --> xem chi tiết 1 khóa học
    # (PUT) --> cập nhật
    # (DELETE) --> xóa khóa học

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

