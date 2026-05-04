from rest_framework import serializers
from .models import Subject, SchoolClass, TeacherProfile, StudentProfile


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class SchoolClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = "__all__"


class TeacherProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = "__all__"


class StudentProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = "__all__"
