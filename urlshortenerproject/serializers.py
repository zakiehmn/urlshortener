from rest_framework import serializers
from .models import Staff
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        exclude = ('id', 'last_login', 'is_superuser', 'first_name', 
                   'last_name', 'is_staff', 'is_active', 'date_joined', 
                   'groups', 'user_permissions')
    
    def create(self, validated_data):
        user = User(
            email = validated_data['email'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class StaffSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Staff
        fields = ('user', 'name','remaining_links', 'active_links',)
        depth = 1
        
        

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        staff, created = Staff.objects.update_or_create(user=user,
                                                        name=validated_data.pop('name'), 
                                                        )
        return staff
