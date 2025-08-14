from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializer import UserSerializer

class UserGenericList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

