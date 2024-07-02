from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import  status 
from django.shortcuts import  get_object_or_404 
from django.http import JsonResponse

@api_view(['POST']) 
def login(request):
    user = get_object_or_404(User, email=request.data['email'])
    
    if not user.check_password(request.data['password']):
     return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)  
  
    token, created = Token.objects.get_or_create(user = user)   
    serializer = UserSerializer(instance=user)
    
    return Response({'token': token.key ,'user': serializer.data},status=status.HTTP_201_CREATED)

@api_view(['POST']) 
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()   
        
        Usuario = User.objects.get(username=serializer.data['username'])
        Usuario.set_password(serializer.data['password'])
        Usuario.save()
        
        token = Token.objects.create(user = Usuario)
        return Response({'token': token.key,'user': serializer.data},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
def forgot_password(request):
   
    user = get_object_or_404(User, id=request.data.get('id'))
        
    user.set_password(request.data.get('password'))
    user.save()
    
    data = {
            'message': 'Contraseña restablecida con éxito'
        }
    return Response(data, status=status.HTTP_200_OK)
  
    