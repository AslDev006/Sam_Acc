from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_Model
        fields = '__all__'