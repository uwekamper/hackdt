from django.forms import widgets
from rest_framework import serializers

from models import *

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('name', 'user')