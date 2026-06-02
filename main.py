from fastapi import FastAPI

# 1. Iniciamos la aplicación
app = FastAPI()

# 2. Simulamos las lecturas de nuestro sensor 🌡️💧
temp_actual = 24.5
hum_actual = 60.0

# 3. Creamos la ruta de ambos datos
@app.get("/datos")
def obtener_datos():
    return {"temperatura": temp_actual, "humedad": hum_actual}

# 4. Creamos la ruta de temperatura
@app.get("/temperatura")
def obtener_temperatura():
    return {"temperatura": temp_actual}

# 5. Creamos la ruta de humedad
@app.get("/humedad")
def obtener_humedad():
    return{"humedad": hum_actual}