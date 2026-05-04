from django.db import models
from apps.accounts.models import User


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    qualification = models.CharField(max_length=100)
    classes = models.ManyToManyField(
        "SchoolClass", blank=True
    )  # teacher teach multiple class

    def __str__(self):
        return self.user.email


class SchoolClass(models.Model):
    name = models.CharField(max_length=100)
    section = models.CharField(max_length=50)
    subjects = models.ManyToManyField(Subject)  # one class has many subject
    class_teacher = models.ForeignKey(
        TeacherProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="class_teacher_of",
    )  # one responsible class teacher

    def __str__(self):
        return f"{self.name} - {self.section}"


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )  # one student has many class
    admission_number = models.CharField(max_length=50)
    classes = models.ManyToManyField(SchoolClass)

    def __str__(self):
        return self.user.email
