from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        field = User
        fields = ('id', 'username', 'email', 'password')

    def create(self,Validated_data):
        return User.objects.create_user(**Validated_data)
        