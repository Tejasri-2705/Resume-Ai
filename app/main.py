from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import user_routes
from app.routes import resume_routes

app = FastAPI(title="Titan Resume AI")

app.include_router(user_routes.router)
app.include_router(resume_routes.router)

# serve UI
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

@app.get("/health")
def health_check():
    return {"status": "Titan Backend Running"}