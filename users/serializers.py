from rest_framework import serializers
from .models import CustomUser
from .models import Child
# Create the serializer class
class UserSerializer(serializers.ModelSerializer):

     # Configure the serializer in the Meta class
    class Meta:
        # Tell the serializer which model to translate
        model = CustomUser
        # Specify which fields to include in the translation
        fields = ['id', 'first_name', 'last_name', 'email', 'role']

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['id','parent','first_name','last_name','date_of_birth']


