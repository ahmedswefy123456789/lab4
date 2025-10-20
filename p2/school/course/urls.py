from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/manual-add/', views.manual_student_create, name='student_manual_add'),
    path('students/', views.StudentListView.as_view(), name='student_list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student_add'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('students/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student_edit'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_add'),
    path('courses/<str:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/<str:pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('courses/<str:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
]
