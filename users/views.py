from django.shortcuts import render
from rest_framework import generics , permissions
from .models import CustomUser
from .serializers import UserSerializer
from .models import Child
from .serializers import ChildSerializer
from .permissions import IsParentOfChildOrAdmin

class UserGenericList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class ChildGenericList(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Child.objects.all()
        elif user.role == 'parent':
            return Child.objects.filter(parent = user)
        return Child.objects.none()
    # this ensures a parent is automatically assigned
    def perform_create(self, serializer):
        if self.request.user.role == 'parent':
            serializer.save(parent=self.request.user)
        else:
            serializer.save()

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [permissions.IsAuthenticated, IsParentOfChildOrAdmin]