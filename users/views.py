from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializer import UserSerializer
from .models import Child
from .serializer import ChildSerializer

class UserGenericList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ChildGenericList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer