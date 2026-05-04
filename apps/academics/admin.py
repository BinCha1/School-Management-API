from django.contrib import admin
from .models import Subject, SchoolClass, StudentProfile, TeacherProfile

admin.site.register(Subject)
admin.site.register(SchoolClass)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
