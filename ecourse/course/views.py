from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from .views import *
from django.views import View
# django-rest
from rest_framework import viewsets, permissions
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

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
    




class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

    # cung cấp API ẩn một cái Lesson đi(active=False)
    @action(methods=['POST'], detail=True, url_path="hide-lesson", url_name="hide-lesson")
    def hide_lesson(self, request, pk):
        try:
            l = Lesson.objects.get(pk=pk)
            l.active = False
            l.save()
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data=LessonSerializer(l, context={'request':request}).data, status=status.HTTP_200_OK)



