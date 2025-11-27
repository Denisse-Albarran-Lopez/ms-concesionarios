from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.concesionaria_controller import router as concesionaria_router
from app.database import create_tables

app = FastAPI(title="MS-Concesionarios", description="Microservicio de concesionarias para CaFES Check")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(concesionaria_router, prefix="/concesionarias", tags=["Concesionarias"])

@app.on_event("startup")
def startup_event():
    create_tables()

@app.get("/")
def read_root():
    return {"message": "MS-Concesionarios - Microservicio de Concesionarias"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)