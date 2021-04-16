import json
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer, UpdateUserSerializer, TicketSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from .models import Ticket


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class SigninView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user_details = User.objects.filter(username=request.user).values()[0]
        print(user_details)
        content = {'message': 'User {} successfully logedin'.format(user_details['username']),
                   'First Name' : user_details['first_name'], 'Last Name' : user_details['last_name'],
                   'EmailId' : user_details['email'], 'is_Admin' : user_details['is_superuser']}
        return Response(content)

class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UpdateUserSerializer

class TicketAPIView(APIView):
    def post(self, request):
        #print(request.data['message'])
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        save_status = serializer.save(userid=request.user, message=request.data['message'])
        return Response(status=status.HTTP_201_CREATED)

class ListTicketView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            user_details = User.objects.filter(username=request.user, is_superuser=1).values()[0]
            all_tickets = Ticket.objects.all()
            content = [{'TicketId' : tk['id'], 'User Id' : tk['userid'], 'Message' : tk['message']} for tk in all_tickets.values()]
        except IndexError:
            content = {'message' : "User {} has no permission to list customer support tickets".format(request.user)}
        return Response(content)