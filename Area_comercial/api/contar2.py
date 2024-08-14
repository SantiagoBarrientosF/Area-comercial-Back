from Area_comercial.api.serializer import *
from Area_comercial.models import Ofertas
from rest_framework.views import APIView
from rest_framework import status 
from collections import Counter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
        informes = Ofertas.objects.all()
        estado_contado = Counter(Informe.Estado for Informe in informes if Informe.Estado in estados_contar)
        return JsonResponse({'estados_contador': dict(estado_contado)}, status=status.HTTP_200_OK)   
    
    
    
class ContarestadoMes(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        estados_contar_negado = {
            'Negado' : 'Negado',
        }
        estados_contar_cerrado = {
            'Cerrado' : 'Cerrado',
        }
        informes = Ofertas.objects.all()
        estados_por_mes = defaultdict(Counter)
        estados_por_mes_cerrados = defaultdict(Counter)
        
        for informe in informes:
            if informe.Estado in estados_contar_negado:
                estados_por_mes[informe.Mes][informe.Estado] += 1
            
            if informe.Estado in estados_contar_cerrado:    
                estados_por_mes_cerrados[informe.Mes][informe.Estado] += 1
                
        estados_por_mes = [{mes: dict(contador) for mes, contador in estados_por_mes.items()}]
        estados_por_mes_cerrados = [{mes: dict(contador) for mes, contador in estados_por_mes_cerrados.items()}]
                
        return JsonResponse({'estados negados por mes': estados_por_mes,'estados cerrados por mes':estados_por_mes_cerrados}, status=status.HTTP_200_OK)
    
class FiltrarTipificacion(APIView):
    def get(self, request):
        estado_buscado = request.query_params.get('Estado', None)
        
        if estado_buscado:
            informes = Ofertas.objects.filter(Estado=estado_buscado)
        else:
            informes = Ofertas.objects.all()
        
        estado_contado = Counter(Informe.Estado for Informe in informes)
        
        return JsonResponse({'estado_contado': dict(estado_contado)})