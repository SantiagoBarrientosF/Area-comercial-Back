from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from .utils.email_utils import send_email 
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, email=request.data['email'])
    
    if not user.check_password(request.data['password']):
        return Response({"error": "Credenciales incorrectas"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data['password'])
        user.save()
        
        token = Token.objects.create(user=user)
        
        # Configura el contexto para el correo electrónico
        context = {
            'username': user.username,
            'protocol': request.scheme,
            'domain': request.get_host(),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
            'site_name': 'Mi Sitio Web'
        }
        
        # Enviar correo de confirmación de registro
        send_email(
            subject='Bienvenido a Mi Sitio Web',
            to_email=user.email,
            context=context,
            html_template='registration/welcome_email.html',
            text_template='registration/welcome_email.txt'
        )
        
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
