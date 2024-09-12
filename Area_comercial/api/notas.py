from Area_comercial.models import Notas,Ofertas
from Area_comercial.api.serializer import NotasSerializer
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse  
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .utils.encryption import *
from datetime import date

class noterequest(APIView):
    def get(self,request):
     items = Notas.objects.all()
     items_list = list(items.values()) 
     return JsonResponse(items_list, safe=False)
 
    def post(self,request):
          if request.method == 'POST':
            titulo = request.data.get('titulo')
            descripcion = request.data.get('descripcion')
            oferta_id = request.data.get('oferta')
          if titulo and descripcion:
            dates = date.today()
            ofertas = Ofertas.objects.get(id=oferta_id)
            notas_ = Notas(
                  titulo = titulo,
                  descripcion = descripcion,
                  fecha = dates,
                  ofertas = ofertas
            )
            notas_.save()
            
            last_item = Notas.objects.all().select_related('ofertas').latest('id')
            
            empresa_data = {
                'id': last_item.ofertas.Cliente.id,
                'nombre': last_item.ofertas.Cliente.Nombre_empresa,  
            }
            item_dict = {
                'id': last_item.id,
                'titulo': last_item.titulo,
                'descripcion': last_item.descripcion,
                'fecha': last_item.fecha,
                'empresa': empresa_data,
                
            }
            
            return JsonResponse({'data':item_dict}, safe=False)
           
   
class Update_notas(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        Nota = get_object_or_404(Notas, id=id)
        Nota.titulo = request.data.get('titulo')
        Nota.descripcion = request.data.get('descripcion')
        Nota.save()
        return JsonResponse({'status': 'success', 'message': 'Datos actualizados correctamente'})
    def delete(self,request,id):
        nota = get_object_or_404(Notas,id=id)
        nota.delete()
        return JsonResponse({'status': 'sucess','message':'Nota eliminado correctamente'})
