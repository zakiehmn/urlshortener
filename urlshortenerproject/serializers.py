from rest_framework import serializers
from .models import Staff
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField()
    class Meta:
        model = User
        exclude = ('password', 'id', 'last_login', 'is_superuser', 'first_name', 
                   'last_name', 'is_staff', 'is_active', 'date_joined', 
                   'groups', 'user_permissions')
        # fields = ('username', 'email',)
        # write_only_fields = ('password',)


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
