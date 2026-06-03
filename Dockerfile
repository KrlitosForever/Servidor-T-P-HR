# 1. Usamos una imagen oficial de Python ligera
FROM python:3.11-slim

# 2. Le decimos a Docker en qué carpeta de la "computadora virtual" vamos a trabajar
WORKDIR /app

# 3. Copiamos el archivo de requisitos a la carpeta de trabajo
COPY requirements.txt .

# 4. Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el código de nuestra API al contenedor
COPY main.py .

# 6. Exponemos el puerto 8000 para que podamos conectarnos
EXPOSE 8000

# 7. El comando para encender el servidor cuando arranque el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]