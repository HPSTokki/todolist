from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from src.exception import DomainException

app = FastAPI()

ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.exception_handler(DomainException)
async def handle_exception(req: Request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.message
        }
    )

@app.get("/health/me", status_code=201)
async def health_check():
    return {
        "ok": True 
    }