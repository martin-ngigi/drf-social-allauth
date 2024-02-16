from rest_framework import serializers
from django.contrib.auth.models import User
from django.core import serializers as my_serializers
import json


def serialize_user(user):
    user_data = my_serializers.serialize('json', [user])
    user_json = json.loads(user_data)[0]['fields']
    return user_json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        # fields = '__all__'
