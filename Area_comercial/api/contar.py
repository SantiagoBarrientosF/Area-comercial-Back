from Area_comercial.api.serializer import *
from Area_comercial.models import Informe
from rest_framework.views import APIView
from rest_framework import status 
from collections import Counter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import InformeSerializer
from django.http import JsonResponse
from collections import defaultdict

class Contarestados(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        estados_contar = {
           'Analisis por el cliente' :'Analisis por el cliente',
           'Cerrado' : 'Cerrado',
           'Negado' : 'Negado',
        }
           
        informes = Informe.objects.all()
        estado_contado = Counter(Informe.Estado for Informe in informes if Informe.Estado in estados_contar)
               
        return JsonResponse({'estados_contador': dict(estado_contado)}, status=status.HTTP_200_OK)   
    
    
    
class ContarestadoMes(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        estados_contar = {
           'Analisis por el cliente' :'Analisis por el cliente',
           'Cerrado' : 'Cerrado',
           'Negado' : 'Negado',
        }
        informes = Informe.objects.all()
        estados_por_mes = defaultdict(Counter)

        for informe in informes:
            if informe.Estado in estados_contar:
                estados_por_mes[informe.Mes][informe.Estado] += 1
                
     
        estados_por_mes = {mes: dict(contador) for mes, contador in estados_por_mes.items()}
                
        return JsonResponse({'estados_por_mes': estados_por_mes}, status=status.HTTP_200_OK)

        
        
        
   