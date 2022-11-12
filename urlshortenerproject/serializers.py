from dataclasses import fields
from unicodedata import name
from rest_framework import serializers
from .models import Staff, Shortener
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


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
    class Meta():
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

class LoginSerializer(StaffSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, user):
        token = Token.objects.get_or_create(user=user.user)
        return token[0].key

    class Meta(StaffSerializer.Meta):
        fields = StaffSerializer.Meta.fields + ('token',)

class ShortenerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta():
        model = Shortener
        fields = ('user','created','long_url','short_url',)
        depth = 1   

        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = StaffSerializer.create(UserSerializer(), data=user_data)
        shortener = Shortener.objects.get_or_create(user=user,
                                                       long_url=validated_data.pop('long_url'),
                                                       short_url=validated_data.pop('short_url'),
                                                       )
        return shortener

    
