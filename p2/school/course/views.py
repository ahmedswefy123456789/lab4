from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Student, Course
from .forms import StudentForm, CourseForm
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
import os


def home(request):
	"""Simple home page linking to students and courses."""
	return render(request, 'course/home.html')


@require_http_methods(['GET', 'POST'])
def manual_student_create(request):
	"""Demonstrate a manual HTML form (not ModelForm) to create a Student.

	Fields handled: name, age, date_of_birth, image (file), courses (multiple checkboxes).
	"""
	if request.method == 'POST':
		name = request.POST.get('name')
		age = request.POST.get('age') or None
		dob = request.POST.get('date_of_birth') or None
		# Create student instance
		student = Student(name=name)
		if age:
			try:
				student.age = int(age)
			except ValueError:
				student.age = None
		if dob:
			student.date_of_birth = dob

		# handle image upload
		if 'image' in request.FILES:
			student.image = request.FILES['image']

		student.save()

		# handle courses - checkboxes named 'course_<code>' or a list named 'courses'
		courses_post = request.POST.getlist('courses')
		if courses_post:
			for code in courses_post:
				try:
					c = Course.objects.get(code=code)
					student.courses.add(c)
				except Course.DoesNotExist:
					continue

		return redirect('course:student_detail', pk=student.pk)

	# GET: show manual form with available courses
	courses = Course.objects.all()
	return render(request, 'course/manual_student_form.html', {'courses': courses})


class StudentListView(generic.ListView):
	model = Student
	template_name = 'course/student_list.html'


class StudentDetailView(generic.DetailView):
	model = Student
	template_name = 'course/student_detail.html'


class StudentCreateView(generic.CreateView):
	model = Student
	form_class = StudentForm
	template_name = 'course/student_form.html'
	success_url = reverse_lazy('course:student_list')


class StudentUpdateView(generic.UpdateView):
	model = Student
	form_class = StudentForm
	template_name = 'course/student_form.html'
	success_url = reverse_lazy('course:student_list')


class StudentDeleteView(generic.DeleteView):
	model = Student
	template_name = 'course/student_confirm_delete.html'
	success_url = reverse_lazy('course:student_list')


class CourseListView(generic.ListView):
	model = Course
	template_name = 'course/course_list.html'


class CourseDetailView(generic.DetailView):
	model = Course
	template_name = 'course/course_detail.html'


class CourseCreateView(generic.CreateView):
	model = Course
	form_class = CourseForm
	template_name = 'course/course_form.html'
	success_url = reverse_lazy('course:course_list')


class CourseUpdateView(generic.UpdateView):
	model = Course
	form_class = CourseForm
	template_name = 'course/course_form.html'
	success_url = reverse_lazy('course:course_list')


class CourseDeleteView(generic.DeleteView):
	model = Course
	template_name = 'course/course_confirm_delete.html'
	success_url = reverse_lazy('course:course_list')
