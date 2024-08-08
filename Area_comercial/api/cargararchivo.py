import pandas as pd
from django.http import JsonResponse
from Area_comercial.models import Ofertas,Empresa
import io
from rest_framework.decorators import api_view

@api_view(['POST'])
def Cargararchivo(request):
    file = request.FILES.getlist("file")
    Ofertas.objects.all().delete()
    for file in file:
        try:
            df = pd.read_excel(io.BytesIO(file.read()), usecols=[
                "MES","CLIENTES", "NUEVO (SI/NO)", "DESCRIPCION",
                "ESTADO", "MENSUAL","POR CAMPAÑA", 
                "SECTOR", "CANAL O MEDIO ", 
                "CAUSAL NEGACION"
            ], sheet_name='2024')
           
            for index, row in df.iterrows():
                data, created = Empresa.objects.get_or_create(
                     Nombre_empresa=row['CLIENTES'],
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
                   
                )
                
                

        except ValueError as e:
            print(f"Error al leer el archivo Excel: {e} {file}")
            return JsonResponse({'error': 'Hubo un error al leer el archivo Excel.'}, status=400)
    
    # Si todo va bien, devolver una respuesta de éxito
    return JsonResponse({'message': 'Archivos cargados exitosamente.'})
