from rest_framework import serializers
from .models import Student
from .models import School


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','firstname','lastname','nationality','age')
        depth = 1

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=('id','name','student','maxstudent','location')
        depth = 2
