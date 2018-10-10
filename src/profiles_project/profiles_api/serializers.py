from rest_framework import serializers
from .models import *
class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView """

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for user profile objects"""

    class Meta:
        model = UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new user """

        user = UserProfile(
            email = validated_data['email'],
            name = validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ A serializer for profile feed items. """
    
    class Meta:
        model = ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}


