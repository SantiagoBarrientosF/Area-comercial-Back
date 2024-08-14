import pandas as pd
from django.http import JsonResponse
from Area_comercial.models import Ofertas,Empresa,Notas
import io
from rest_framework.decorators import api_view
from Area_comercial.api.serializer import NotasSerializer

@api_view(['POST'])
def Cargararchivo(request):
    file = request.FILES.getlist("file")
    Ofertas.objects.all().delete()
    Notas.objects.all().delete()
    for file in file:
        try:
            df = pd.read_excel(io.BytesIO(file.read()), usecols=[
                "MES","CLIENTES", "NUEVO (SI/NO)", "DESCRIPCION",
                "ESTADO", "MENSUAL","POR CAMPAÑA", 
                "SECTOR", "CANAL O MEDIO ", 
                "CAUSAL NEGACION"
            ], sheet_name='2024')
           
            for index, row in df.iterrows():
             if pd.notnull(row['MES']) or pd.notnull(row['CLIENTES']) or pd.notnull(row['NUEVO (SI/NO)']) or pd.notnull(row['DESCRIPCION']) or pd.notnull(row['ESTADO']) or pd.notnull(row['MENSUAL']) or pd.notnull(row['POR CAMPAÑA']) or pd.notnull(row['SECTOR']) or pd.notnull(row['CANAL O MEDIO ']) or pd.notnull(row['CAUSAL NEGACION']): 
                data, created = Empresa.objects.get_or_create(
                     Nombre_empresa=row['CLIENTES'],
                )
                nota = Notas.objects.create(
                     notas = ""
                 )
                Ofertas.objects.create(
                    Mes=row['MES'],
                    Cliente = data,
                    Nuevo=row['NUEVO (SI/NO)'],
                    Descripcion=row['DESCRIPCION'],
                    Estado=row['ESTADO'],
                    Pago_mensual=row['MENSUAL'],
                    Por_campaña=row['POR CAMPAÑA'],
                    Sector=row['SECTOR'],
                    Canal_medio=row['CANAL O MEDIO '],
                    Causal_negacion=row['CAUSAL NEGACION'],
                    notas = nota
                )
                
        except ValueError as e:
            print(f"Error al leer el archivo Excel: {e} {file}")
            return JsonResponse({'error': 'Hubo un error al leer el archivo Excel.'}, status=400)
    ids = list(Notas.objects.values_list('id', flat=True))        
    return JsonResponse({'data':ids, 'message': 'Archivos cargados exitosamente.'})
