# Prueba de caja negra, simulando un timeout
# no controlamos la API (en teoría)
# No tienes acceso al código

# region 1
# import time
# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get("/")
# async def index():
#     return "Pruebas hacia Fast API"
#
#
# # Eliminar despues de explicar que la prueba pasa
# @app.get("/timeout")
# async def timeout():
#     time.sleep(5)
#     return "Exito!!"

# endregion

import time
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return "Pruebas hacia Fast API"


# Eliminar despues de explicar que la prueba pasa
@app.get("/timeout")
async def timeout():
    time.sleep(10)
    return "Exito!!"

