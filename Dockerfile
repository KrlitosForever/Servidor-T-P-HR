# 1. Usamos una imagen oficial de Python ligera
FROM python:3.11-slim

# NUEVO: Instalamos la librería del sistema para los pines GPIO
RUN apt-get update && apt-get install -y libgpiod2 && rm -rf /var/lib/apt/lists/*

# 2. Le decimos a Docker en qué carpeta trabajar
WORKDIR /app

# 3. Copiamos el archivo de requisitos
COPY requirements.txt .

# 4. Instalamos las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el código
COPY main.py .

# 6. Exponemos el puerto
EXPOSE 8000

# 7. El comando para encender el servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]