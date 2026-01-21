#Importaciones
from fastapi import FastAPI
from routers import articulo

#Se define la api
app= FastAPI()

@app.get("/")
def prueba():
    return {"mensaje":"hola mundo"}

#Endpoint para articulo
app.include_router(articulo.router)
