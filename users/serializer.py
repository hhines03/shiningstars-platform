from rest_framework import serializers
from .models import CustomUser

# Create the serializer class
class UserSerializer(serializers.ModelSerializer):

     # Configure the serializer in the Meta class
    class Meta:

        # Tell the serializer which model to translate
        model = CustomUser

        # Specify which fields to include in the translation
        fields = ['id', 'first_name', 'last_name', 'email', 'role']

