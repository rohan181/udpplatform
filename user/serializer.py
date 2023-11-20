from rest_framework import serializers

from . import services
from rest_framework import serializers
from .models import User,Profileinfo1,Profileinfolocationbd,Profileinfolocationabroad,Profileinfoexperience,Profilecomplete1, Profilecomplete2, Profilecomplete3, Profilecomplete4, Profilecomplete5


class UserCreateSerializerphone(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('phone_number', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Create a user with the provided data
        user = User.objects.create_user(**validated_data)
        return user
    


class UserCreateSerializeremail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Create a user with the provided data
        user = User.objects.create_user(**validated_data)
        return user   



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    firstname = serializers.CharField()
   
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)
    

class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profileinfo1
        fields = ('user_name', 'gender', 'date_of_birth','profilephoto')  # Include only the fields that users can provide when creating a profile


class Profileloactionbd(serializers.ModelSerializer):
    class Meta:
        model = Profileinfolocationbd
        fields = ('District',)



class Profileloactionabroad(serializers.ModelSerializer):
    class Meta:
        model = Profileinfolocationabroad
        fields = ('countryname','city','duration')   







class Profileinfoexperienceserializer(serializers.ModelSerializer):
    class Meta:
        model = Profileinfoexperience
        fields = ('durationstay','industry','areaofexpertise','durationstay','durationstayexperience')  






class Profilecomplete1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profilecomplete1
        exclude = ('user',)

class Profilecomplete2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profilecomplete2
        exclude = ('user',)

class Profilecomplete3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profilecomplete3
        exclude = ('user',)

class Profilecomplete4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profilecomplete4
        exclude = ('user',)

class Profilecomplete5Serializer(serializers.ModelSerializer):
    class Meta:
        model = Profilecomplete5
        exclude = ('user',)


