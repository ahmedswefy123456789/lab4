from django.contrib import admin
from .models import Student, Course, StudentCourse


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'date_of_birth')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course')
from django.contrib import admin

# Register your models here.
