from Area_comercial.models import Empresa,Ofertas,Notas
from Area_comercial.api.serializer import EmpresaSerializer,OfertasSerializer
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse  
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class Showofertas(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]  
   def get(request,self):
      
    items = Ofertas.objects.all()
    items_list = list(items.values()) 
    return JsonResponse(items_list, safe=False) 
 
   def post(self,request):
      if request.method == 'POST':
        Mes = request.data.get('mes') 
        Nuevo = request.data.get('nuevo')
        Descripcion = request.data.get('descripcion')
        Estado = request.data.get('estado')
        Pago_mensual = request.data.get('pago_mensual')
        Sector = request.data.get('sector')   
        Causal_negacion = request.data.get('causal_negacion')   
        Por_campaña = request.data.get('por_campaña')   
        Canal_medio = request.data.get('canal_medio')   
        Cliente = request.data.get('cliente')  
        notas = request.data.get('notas') 
      if Mes and Nuevo and Descripcion and Estado and Pago_mensual and Sector and Causal_negacion and Por_campaña and Canal_medio and Cliente and notas:
       data_nota = Notas(
          notas = notas
       )
       data_nota.save()
       data = Ofertas(
            Mes = Mes,
            Nuevo = Nuevo,
            Descripcion = Descripcion,
            Estado = Estado,
            Pago_mensual = Pago_mensual,
            Sector = Sector,   
            Causal_negacion = Causal_negacion,   
            Por_campaña = Por_campaña,   
            Canal_medio = Canal_medio, 
            Cliente = Cliente,
            notas_id = data_nota.id
       )
       data.save()
       ultimo_contacto = Ofertas.objects.last()
       serializer_contacto = OfertasSerializer(ultimo_contacto)  
    
      return JsonResponse({'data': serializer_contacto.data, 'message' : 'Oferta agregada correctamente'})        
    
    
class Update_ofertas(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        ofertas = get_object_or_404(Ofertas, id=id)
        ofertas.Descripcion = request.data.get('descripcion')
        ofertas.Estado = request.data.get('Estado')
        ofertas.Pago_mensual = request.data.get('pago_mensual')
        ofertas.Sector = request.data.get('sector')   
        ofertas.Causal_negacion = request.data.get('causal_negacion')   
        ofertas.Por_campaña = request.data.get('por_campaña')   
        ofertas.Canal_medio = request.data.get('canal_medio')   
        ofertas.Cliente = request.data.get('cliente')  
        ofertas.save()

            