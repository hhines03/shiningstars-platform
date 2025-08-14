from django.urls import path
from .views import UserGenericList

urlpatterns = [
    path('users/', UserGenericList.as_view(), name = 'user-list')
]