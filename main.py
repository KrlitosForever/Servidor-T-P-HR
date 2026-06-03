from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. Configuración CORS ultra permisiva para desarrollo local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # El asterisco significa: "Permite que CUALQUIER página web consulte esta API"
    allow_credentials=False, # Debe estar en False cuando usamos el asterisco "*"
    allow_methods=["*"],  # Permite GET, POST, etc.
    allow_headers=["*"],  # Permite cualquier encabezado
)

# 2. Simulamos las lecturas de nuestro sensor 🌡️💧
temp_actual = 24.5
hum_actual = 60.0

# 3. Tus rutas de datos
@app.get("/datos")
def obtener_datos():
    return {"temperatura": temp_actual, "humedad": hum_actual}

@app.get("/temperatura")
def obtener_temperatura():
    return {"temperatura": temp_actual}

@app.get("/humedad")
def obtener_humedad():
    return {"humedad": hum_actual}