import pandas as pd
from django.http import HttpResponse
import io
from Area_comercial.models import *
from rest_framework.views import APIView


class Exportecomercial(APIView):
   def get(self, request):   
       
    datos = []
    ofertas = Ofertas.objects.all().select_related('Cliente')
    notas  =Notas.objects.all().select_related('ofertas')
    for oferta in ofertas:
        item = Notas.objects.all()
        datos.append({
                'Empresa': oferta.Cliente.Nombre_empresa,
                'Descripcion':oferta.Descripcion,
                'Estado':oferta.Estado,
                'Mensual':oferta.Pago_mensual,
                'Por campaña':oferta.Por_campaña,
                'Sector':oferta.Sector,
                'Canal o medio':oferta.Canal_medio,
                'Causal negacion':oferta.Causal_negacion,

            })
    
   
    df = pd.DataFrame(datos)
    
    
    output = io.BytesIO()
    
    
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False)
    
    response = HttpResponse(output.getvalue(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=ofertas.xlsx'
    
    return response