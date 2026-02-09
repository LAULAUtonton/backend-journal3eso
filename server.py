from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS: permitir frontend de Netlify
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://journal3eso.netlify.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de prueba
@app.get("/")
def root():
    return {"status": "Backend running"}

# Endpoint que usará tu frontend
@app.get("/api/groups")
def get_groups():
    return []
