from rest_framework import serializers
from .models import User, UseInviteCode


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UseInviteCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseInviteCode
        fields = '__all__'
