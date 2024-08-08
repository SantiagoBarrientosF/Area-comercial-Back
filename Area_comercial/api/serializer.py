
from rest_framework import serializers
from django.contrib.auth.models import User
from Area_comercial.models import Ofertas,Empresa,Notas

# The `UserSerializer` class defines a serializer for the User model with specified fields.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
# The `InformeSerializer` class is a Django REST framework serializer for the `Informe` model with all
# fields included.
class InformeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofertas
        fields = '__all__'        
        
        
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'  
        
        
class NotasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notas
        fields = '__all__'                
        
        
class OfertasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofertas
        fields = '__all__'                
