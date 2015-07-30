from django.db import models
from django.db.models import Q
# Create your models here.

class Student(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	email=models.CharField(max_length=100)
	gpa=models.FloatField(default=0)
	def __str__(self):
		return str(self.first_name)+' '+str(self.last_name)

class Subject(models.Model):
	name=models.CharField(max_length=50)
	def __str__(self): return name

class linking(models.Model):
	student=models.ForeignKey(Student)
	subject=models.ForeignKey(Subject)
	grade=models.FloatField(default=0.0)
	