from django.contrib import admin
from student_interface.models import Student,linking,Subject

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(linking)