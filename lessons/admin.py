from django.contrib import admin
from lessons.models import Lesson, Course


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'owner')
    list_filter = ('name', 'course',)
    search_fields = ('name', 'course', 'owner',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')
    list_filter = ('name', 'description',)
    search_fields = ('name', 'description', 'owner',)