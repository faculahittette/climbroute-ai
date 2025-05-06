from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .models.inference import suggest_routes

app = FastAPI(title="ClimbRoute AI", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "alive"}

@app.post("/predict")
async def predict(image: UploadFile = File(...)):
    try:
        img_bytes = await image.read()
        routes = suggest_routes(img_bytes)
        return {"routes": routes}
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
