from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag, User
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.urls import path
from django.template.response import TemplateResponse
from django.db.models import Count
from django.contrib.auth.models import Permission

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Lesson
        fields = '__all__'


# inline
class LessonTagInline(admin.TabularInline):
    model = Lesson.tags.through




class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('/static/css/main.css', )
        }

    form = LessonForm
    list_display = ['id', 'subject', 'created_date', 'updated_date', 'active', 'content', 'course']
    search_fields = ['subject','course__subject']
    list_filter = ['subject', 'course__subject']

    readonly_fields = ['avatar']

    inlines = (LessonTagInline ,)

    def avatar(self, lesson):
        return mark_safe("<img src='/static/{img_url}' alt='{alt}' width='150px'/>" .format(img_url=lesson.image.name, alt=lesson.subject))
    




class LessonInLine(admin.StackedInline):
    model = Lesson
    pk_name = 'course'

class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInLine, )




class CourseAppAdminSite(admin.AdminSite):
    site_header = 'HE THONG QUAN LY KHOA HOC'

    def get_urls(self):
        return [
            path('course-stats/', self.course_stats),
        ] + super().get_urls()

    def course_stats(self, request):
        course_count = Course.objects.count()
        stats = Course.objects.annotate(lesson_count=Count('lessons')).values('id', 'subject', 'lesson_count')

        return TemplateResponse(request, 'admin/course_stats.html',{
            'course_count' : course_count,
            'stats': stats
        })
    



admin_site = CourseAppAdminSite('mycourse')

admin_site.register(Category)
admin_site.register(Course, CourseAdmin)
admin_site.register(Lesson, LessonAdmin)

# Register your models here.
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(User)
admin.site.register(Permission)