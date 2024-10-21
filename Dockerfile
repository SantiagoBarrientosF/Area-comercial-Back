# Usa una imagen base de Python
FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requirements.txt
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto 8000
EXPOSE 8000

# Comando para iniciar el servidor Django en modo desarrollo
CMD ["gunicorn", "server.wsgi:application", "--bind", "0.0.0.0:8000"]
