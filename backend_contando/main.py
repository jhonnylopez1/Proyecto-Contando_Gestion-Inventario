#Importaciones
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend_contando.routers import articulo

#Se define la api
app= FastAPI()

#CORS: Evita que el navegador bloquee la aplicacion web
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def prueba():
    return {"mensaje":"hola mundo"}

#Endpoint para articulo
app.include_router(articulo.router)
