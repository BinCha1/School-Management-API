from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Subject, SchoolClass, TeacherProfile, StudentProfile
from .serializers import (
    SubjectSerializers,
    SchoolClassSerializers,
    TeacherProfileSerializers,
    StudentProfileSerializers,
)
from apps.accounts.permissions import IsPrincipalUser


# for subject api
class SubjectAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPrincipalUser]

    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializers(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# for class api
class SchoolClassAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPrincipalUser]

    def get(self, request):
        classes = SchoolClass.objects.all()
        serializer = SchoolClassSerializers(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SchoolClassSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# teacher profile api
class TeacherProfileAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPrincipalUser]

    def get(self, request):
        teachers = TeacherProfile.objects.all()
        serializer = TeacherProfileSerializers(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherProfileSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# student api
class StudentProfileAPIView(APIView):
    permission_classes = [IsAuthenticated, IsPrincipalUser]

    def get(self, request):
        students = StudentProfile.objects.all()
        serializer = StudentProfileSerializers(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
