from django.urls import path
from .views import UserGenericList , ChildGenericList , ChildDetail

urlpatterns = [
    path('users/', UserGenericList.as_view(), name = 'user-list'),
    path('children/', ChildGenericList.as_view(), name = 'child-list'),
    path('children/<int:pk>/', ChildDetail.as_view(), name = 'child-detail')
]