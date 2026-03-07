from fastapi import FastAPI

app = FastAPI()

@app.get("/health/me", status_code=201)
async def health_check():
    return {
        "ok": True 
    }