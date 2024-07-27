from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import User
from friendship.models import Friend


class UserSer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'telephone_number',
            'tag_user',
            'birthday',
            'city',
            'country',
            'title'
                  )
        

class UserRegistrationSer(UserCreateSerializer):
    
    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + (
            'telephone_number',
            'first_name',
            'last_name',
            'tag_user',
            'birthday'
            )


class UserProfileSer(UserSerializer):
    
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + (
            'tag_user',
            'first_name',
            'last_name',
            'photo',
            'telephone_number',
            'birthday',
            'city',
            'country',
            'title'
            )
        

class UserFriendsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Friend
        fields = ('to_user', 'from_user')