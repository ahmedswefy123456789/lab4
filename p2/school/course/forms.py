from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'image', 'date_of_birth', 'courses']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']
