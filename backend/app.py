from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importa tus routers
from routes.users import user
from routes.persons import person
from routes.roles import rol
from routes.usuarios_roles import userrol
from routes.lotes import lote

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Puedes especificar dominios específicos si lo prefieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#app.include_router(persona)
app.include_router(user)
app.include_router(person)
app.include_router(rol)
app.include_router(userrol)
app.include_router(lote)



print("Bienvenido a mi Aplicacion")