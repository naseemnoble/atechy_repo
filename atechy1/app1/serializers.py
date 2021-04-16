from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Ticket

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('is_superuser', 'password', 'password2', 'email', 'first_name', 'last_name', 'username', 'is_staff')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'is_superuser': {'required': True},
            'username': {'required': False},
            'is_staff': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            is_superuser=validated_data['is_superuser'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['email'],
            is_staff=validated_data['is_superuser']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class UpdateUserSerializer(serializers.ModelSerializer):
    #email = serializers.EmailField(required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }

    '''
    def validate_email(self, value):
        user = self.context['request'].user
        #print(type(user))
        #print(user.pk)
        #print(value)
        #print(type(value))
        #if User.objects.exclude(pk=user.pk).filter(email=value).exists():
        #    raise serializers.ValidationError({"email": "This email is already in use."})
        return value'''

    def update(self, instance, validated_data):
        instance =  self.context['request'].user
        print(instance)
        print(type(instance))
        print(validated_data)
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.save()
        return instance

class TicketSerializer(serializers.ModelSerializer):
    #userid = serializers.CharField(required=False)
    class Meta:
        model = Ticket
        fields = ['message']

