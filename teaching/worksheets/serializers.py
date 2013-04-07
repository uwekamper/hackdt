from django.forms import widgets
from rest_framework import serializers

from models import *

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', 'user')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student