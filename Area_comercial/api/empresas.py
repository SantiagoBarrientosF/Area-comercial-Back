from Area_comercial.models import Empresa,Ofertas,Notas
from Area_comercial.api.serializer import EmpresaSerializer,OfertasSerializer
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse  
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .utils.encryption import *


class empresa_request(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]  
   def get(request,self):
    items = Empresa.objects.all()
    items_list = [] 
    for item in items: 
       if item.Estado == 'Habilitado' and 'habilitado':
          item_dict ={
             'id':item.id,
             'Nombre_empresa':item.Nombre_empresa,
             'Email':item.Email,
             'Encargado':item.Encargado,
             'Telefono':item.Telefono,
             'nuevo':item.Nuevo
          }       
          items_list.append(item_dict)
    return JsonResponse(items_list, safe=False)

   def post(self,request):
      if request.method == 'POST':
         Nombre_empresa = request.data.get('Nombre_empresa')
         Nuevo = request.data.get('nuevo')
         Encargado = request.data.get('Encargado')
         Telefono = request.data.get('Telefono')
         Email = request.data.get('Email')
      if Nombre_empresa and Encargado and Telefono and Email and Nuevo:
         
         empresas = Empresa(
               Nombre_empresa = Nombre_empresa,
               Nuevo = Nuevo,
               Encargado = Encargado,
               Telefono = Telefono,
               Email = Email     
         )
         empresas.save()
        
         ultimo_contacto = Empresa.objects.last()
         serializer_ofertas = EmpresaSerializer(ultimo_contacto)  
   
         return JsonResponse({'data': serializer_ofertas.data,'message': 'Datos guardados correctamente'}) 
  
class Update_empresa(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        empresa = get_object_or_404(Empresa, id=id)
        empresa.Nombre_empresa = request.data.get('Nombre_empresa')
        empresa.Nuevo = request.data.get('nuevo')
        empresa.Encargado = request.data.get('encargado')
        empresa.Telefono = request.data.get('telefono')
        empresa.Email = request.data.get('email')   
        empresa.Estado = request.data.get('estado')
        empresa.save()
        
        return JsonResponse({'status': 'success', 'message': 'Datos actualizados correctamente'})
