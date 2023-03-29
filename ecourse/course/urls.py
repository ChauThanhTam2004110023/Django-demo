from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from .admin import admin_site
# rest
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('courses', views.CourseViewSet)


urlpatterns = [
    path('', views.index, name='index'),
    path('admin-site/', admin_site.urls),

    
    path('welcome/<int:year>/', views.welcome, name='welcome'),
    re_path(r'welcome2/(?P<year>[0-9]{4})/$', views.welcome2, name='welcome2'),
    
    path('test/<int:year>/', views.TestView.as_view()),


    path('', include(router.urls))
    # với khai này nó sẽ tạo ra Api tương ứng vs 5 API
    # /courses/ - GET
    # /courses/ - POST
    # /courses/ {course_id}/ - GET
    # /courses/ {course_id}/ - PUT
    # /courses/ {course_id}/ - DELETE
]


