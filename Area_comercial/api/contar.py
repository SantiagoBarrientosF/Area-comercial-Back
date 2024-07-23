from Area_comercial.api.serializer import *
from Area_comercial.models import Informe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from collections import Counter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date
from django.http import JsonResponse

class Contarestados(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        
        Meses = {
            'Enero' : 1,
            'Febrero' : 2,
            'Marzo' : 3,
            'Abril' : 4,
            'Mayo' : 5,
            'Junio' : 6,
            'Julio' : 7,
            'Agosto' : 8,
            'Septiembre' : 9,
            'Octubre' : 10,
            'Noviembre' : 11,
            'Diciembre' : 12,
            
        }
        # Today = date.today()
        # Mes_actual = Today.month
        # print(Mes_actual)
        # print (Meses)
        # if Mes_actual in Meses:
        estados_contar = {
            'Analisis por el cliente' :'Analisis por el cliente',
            'Cerrado' : 'Cerrado',
            'Negado' : 'Negado',
         }
            
        informes = Informe.objects.all()

        estado_contado = Counter(Informe.Estado for Informe in informes if Informe.Estado in estados_contar)
                
        return JsonResponse({'estados_contador': dict(estado_contado)}, status=status.HTTP_200_OK)   
        # else:
        #     return JsonResponse({'message':'No se pueden mostrar los datos'}, status=status.HTTP_204_NO_CONTENT)
     
