from django.db import models


class Course(models.Model):
	# use code as primary key per the diagram
	code = models.CharField(max_length=20, primary_key=True)
	name = models.CharField(max_length=200)

	def __str__(self) -> str:
		return f"{self.code} - {self.name}"


class Student(models.Model):
	# id will be the default AutoField primary key
	name = models.CharField(max_length=200)
	age = models.PositiveIntegerField(null=True, blank=True)
	image = models.ImageField(upload_to='student_images/', null=True, blank=True)
	date_of_birth = models.DateField(null=True, blank=True)
	courses = models.ManyToManyField(Course, through='StudentCourse', related_name='students')

	def __str__(self) -> str:
		return self.name


class StudentCourse(models.Model):
	id = models.BigAutoField(primary_key=True)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, to_field='code', on_delete=models.CASCADE)

	class Meta:
		unique_together = ('student', 'course')

	def __str__(self) -> str:
		return f"{self.student} -> {self.course}"
