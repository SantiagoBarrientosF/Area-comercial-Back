from Area_comercial.models import Notas,Empresa
from Area_comercial.api.serializer import NotasSerializer
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse  
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class noterequest(APIView):
    def get(self,request):
     notes = Notas.objects.all()
     notes_list = list(notes.values())
     return JsonResponse(notes_list, safe=False) 
    def post(self,request):
          if request.method == 'POST':
            titulo = request.data.get('titulo')
            descripcion = request.data.get('descripcion')
            fecha = request.data.get('fecha')
            empresa_id = request.data.get('empresa')
          if titulo and descripcion and fecha:
            
            notas = Notas(
                  titulo = titulo,
                  descripcion = descripcion,
                  fecha = fecha
            )
            notas.save()
            empresas = Empresa(
                notas_id = notas.id
            )
            empresas.save()
            ultimo_contacto = Notas.objects.last()
            serializer_ofertas = NotasSerializer(ultimo_contacto)  
      
            return JsonResponse({'data': serializer_ofertas.data,'message': 'Datos guardados correctamente'}) 
   
class Update_notas(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        Nota = get_object_or_404(Notas, id=id)
        Nota.notas = request.data.get('notas')
        Nota.save()
        return JsonResponse({'status': 'success', 'message': 'Datos actualizados correctamente'})
