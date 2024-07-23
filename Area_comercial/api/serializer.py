
from rest_framework import serializers
from django.contrib.auth.models import User
from Area_comercial.models import Informe,Empresa

# The `UserSerializer` class defines a serializer for the User model with specified fields.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
# The `InformeSerializer` class is a Django REST framework serializer for the `Informe` model with all
# fields included.
class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informe
        fields = '__all__'        
        
        
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'        