from Area_comercial.models import Empresa,Ofertas
from Area_comercial.api.serializer import EmpresaSerializer
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse  
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# This class defines a viewset for the "Informe" model in Django, specifying the queryset and
# serializer to be used.
# class Getdata(APIView):
#  authentication_classes = [TokenAuthentication]
#  permission_classes = [IsAuthenticated]    
#  def get(request,self):
#     items = Empresa.objects.all()
#     items_list = list(items.values())  # Convertir los objetos a una lista de diccionarios
#     return JsonResponse(items_list, safe=False)

  
class SaveEmpresa(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]  
   def get(request,self):
    items = Empresa.objects.all()
    items_list = list(items.values()) 
    return JsonResponse(items_list, safe=False)
   def post(self,request):
    if request.method == 'POST':
       Nombre_empresa = request.data.get('Nombre_empresa')
       Encargado = request.data.get('Encargado')
       Telefono = request.data.get('Telefono')
       Email = request.data.get('Email')
    if Nombre_empresa and Encargado and Telefono and Email:
       data = Empresa(
            Nombre_empresa = Nombre_empresa,
            Encargado = Encargado,
            Telefono = Telefono,
            Email = Email     
       )
       data.save()
       ultimo_contacto = Empresa.objects.last()
       serializer_contacto = EmpresaSerializer(ultimo_contacto)  
    
    return JsonResponse({'data': serializer_contacto.data, 'message' : 'Contacto agregado correctamente'}) 
 
class SaveContact(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]  
   def get(request,self):
    items = Empresa.objects.all()
    items_list = list(items.values()) 
    return JsonResponse(items_list, safe=False)
   def post(self,request):
    if request.method == 'POST':
       Nombre_empresa = request.data.get('Nombre_empresa')
       Encargado = request.data.get('Encargado')
       Telefono = request.data.get('Telefono')
       Email = request.data.get('Email')
    if Nombre_empresa and Encargado and Telefono and Email:
       data = Empresa(
            Nombre_empresa = Nombre_empresa,
            Encargado = Encargado,
            Telefono = Telefono,
            Email = Email     
       )
       data.save()
       ultimo_contacto = Empresa.objects.last()
       serializer_contacto = EmpresaSerializer(ultimo_contacto)  
    
    return JsonResponse({'data': serializer_contacto.data, 'message' : 'Contacto agregado correctamente'})  
    
class Update(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        empresa = get_object_or_404(Empresa, id=id)
        empresa.Nombre_empresa = request.data.get('Nombre_empresa')
        empresa.Encargado = request.data.get('Encargado')
        empresa.Telefono = request.data.get('Telefono')
        empresa.Email = request.data.get('Email')   
        empresa.save()
        
        return JsonResponse({'status': 'success', 'message': 'Datos actualizados correctamente'})
     
class Showofertas(APIView):
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]  
   def get(request,self):
    items = Ofertas.objects.all()
    items_list = list(items.values()) 
    return JsonResponse(items_list, safe=False)     