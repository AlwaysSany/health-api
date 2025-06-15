from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from app.core.config import settings
from app.middlewares.cors import add_cors_middleware
from app.api.routes import auth, patients, doctors, appointments, medical_records

app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    description="A comprehensive health microservice API with JWT authentication",
)

# Add CORS middleware
add_cors_middleware(app)

# Include routers
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(doctors.router)
app.include_router(appointments.router)
app.include_router(medical_records.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Health Microservice API"}


@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": settings.version}

# Create an MCP server based on this app
mcp = FastApiMCP(app)

# Mount the MCP server directly to your app
mcp.mount()
