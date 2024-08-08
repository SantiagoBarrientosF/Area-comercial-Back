from Area_comercial.models import Empresa,Ofertas,Notas
from Area_comercial.api.serializer import EmpresaSerializer,OfertasSerializer
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
 

class Update_notas(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, id):
        Nota = get_object_or_404(Notas, id=id)
        Nota.notas = request.data.get('notas')
        Nota.save()
        return JsonResponse({'status': 'success', 'message': 'Datos actualizados correctamente'})
