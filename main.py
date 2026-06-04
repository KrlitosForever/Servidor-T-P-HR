from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import board
import adafruit_ahtx0
import adafruit_bmp280

# 1. Iniciamos la conexión con los pines físicos (I2C)
i2c = board.I2C()

# 2. Le decimos a Python que reconozca los sensores en esa conexión
sensor_aht = adafruit_ahtx0.AHTx0(i2c)
sensor_bmp = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)
# Nota: El BMP280 también mide temperatura, puedes usar la de cualquiera de los dos chips.

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Tus rutas ahora leen el hardware en tiempo real
@app.get("/datos")
def obtener_datos():
    # Leemos la temperatura del AHT20 y la redondeamos a 1 decimal
    temp_real = round(sensor_aht.temperature, 1)
    hum_real = round(sensor_aht.relative_humidity, 1)
    pre_real = round(sensor_bmp.pressure, 1)
    return {"temperatura": temp_real, "humedad": hum_real, "presion": pre_real}

@app.get("/temperatura")
def obtener_temperatura():
    return {"temperatura": round(sensor_aht.temperature, 1)}

@app.get("/humedad")
def obtener_humedad():
    return {"humedad": round(sensor_aht.relative_humidity, 1)}

# Como bonus, ¡ahora también tienes un barómetro gracias al BMP280!
@app.get("/presion")
def obtener_presion():
    return {"presion": round(sensor_bmp.pressure, 1)}