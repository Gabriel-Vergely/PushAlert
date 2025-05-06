from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.post("/webhook")
async def handle_push(request: Request):
    # Obtiene el payload del cuerpo de la solicitud
    payload = await request.json()
    
    # Imprime el payload recibido para depuración
    print("🔔 Webhook recibido desde GitHub:")
    print(payload)  # Imprime el contenido del webhook recibido
    
    # Si quieres imprimir algunos valores específicos del webhook
    print("Repositorio:", payload.get("repository", {}).get("name"))
    print("Evento:", payload.get("ref"))

    return JSONResponse(content={"message": "Push recibido"}, status_code=200)
