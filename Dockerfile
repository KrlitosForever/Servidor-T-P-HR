# 1. Usamos una imagen de Python ligera y fijada a la versión estable Bookworm
FROM python:3.11-slim-bookworm

# 2. Instalamos la librería del sistema y las herramientas de compilación
RUN apt-get update && apt-get install -y libgpiod2 gcc python3-dev && rm -rf /var/lib/apt/lists/*

# 3. Le decimos a Docker en qué carpeta trabajar
WORKDIR /app

# 4. Copiamos el archivo de requisitos
COPY requirements.txt .

# 5. Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copiamos el código
COPY main.py .

# 7. Exponemos el puerto
EXPOSE 8000

# 8. El comando para encender el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]