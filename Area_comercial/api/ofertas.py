from Area_comercial.models import Empresa,Ofertas,Notas
from Area_comercial.api.serializer import EmpresaSerializer,OfertasSerializer,NotasSerializer
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest  
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from .utils.encryption import *


class Showofertas(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]  
   def get(request,self):
    items = Ofertas.objects.all().select_related('Cliente')
    items_list = []
    
    for item in items:
       item_dict = {
          'id': item.id,
          'Nombre_empresa':item.Cliente.Nombre_empresa,
          'descripcion':item.Descripcion,
          'estado':item.Estado,
          'pago_mensual':item.Pago_mensual,
          'por_campaña':item.Por_campaña,
          'sector':item.Sector,
          'canal_medio':item.Canal_medio,
          'cliente':item.Cliente.id,
          'causal_negacion':item.Causal_negacion,
          
       }
       items_list.append(item_dict)
        
    return JsonResponse(items_list, safe=False)
   
   def post(self, request):
        if request.method == 'POST':
            Descripcion = request.data.get('descripcion')
            Estado = request.data.get('estado')
            Pago_mensual = request.data.get('pago_mensual')
            Por_campaña = request.data.get('por_campana')
            Sector = request.data.get('sector')   
            Causal_negacion = request.data.get('causal_negacion')   
            Canal_medio = request.data.get('canal_medio')   
            Cliente_id = request.data.get('cliente')  

            Cliente = Empresa.objects.get(id=Cliente_id)
            
            Month = datetime.now().month
            Year = datetime.now().year
            if Pago_mensual:
                Por_campaña = None  
            else:
                Pago_mensual = None  
            data = Ofertas(
                Mes=Month,
                Descripcion=Descripcion,
                Estado=Estado,
                Pago_mensual=Pago_mensual,
                Sector=Sector,   
                Causal_negacion=Causal_negacion,   
                Por_campaña=Por_campaña,   
                Canal_medio=Canal_medio, 
                Cliente=Cliente,
                Anio = Year
            )
            data.save()
            
           
            last_item = Ofertas.objects.select_related('Cliente').latest('id')
           
            item_dict = {
                'id': last_item.id,
                'Nombre_empresa': last_item.Cliente.Nombre_empresa,
                'descripcion': last_item.Descripcion,
                'estado': last_item.Estado,
                'pago_mensual': last_item.Pago_mensual,
                'por_campana': last_item.Por_campaña,
                'sector': last_item.Sector,
                'canal_medio': last_item.Canal_medio,
                'cliente': Cliente_id,
                'causal_negacion': last_item.Causal_negacion,
                'anio':last_item.Anio
            }
            
            return JsonResponse({'data': item_dict}, safe=False)
        
        return JsonResponse({'error': 'Método no permitido'}, status=405)
   
    
class Update_ofertas(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        ofertas = get_object_or_404(Ofertas, id=id)
        ofertas.Descripcion = request.data.get('descripcion')
        ofertas.Estado = request.data.get('estado')
        ofertas.Pago_mensual = request.data.get('pago_mensual')
        ofertas.Sector = request.data.get('sector')   
        ofertas.Causal_negacion = request.data.get('causal_negacion')   
        ofertas.Por_campaña = request.data.get('por_campana')   
        ofertas.Canal_medio = request.data.get('canal_medio')   
        ofertas.save()
        
        return JsonResponse({'status': 'success', 'message': 'Datos actualizados correctamente'})    
     
     
     


  
   