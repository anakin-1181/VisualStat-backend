from fastapi import FastAPI
from app.core.distribution import generate_distribution
from app.models.model import Plotparams
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Response

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.head("/health")
async def health_head():
    # Return only headers, no JSON body
    return Response(status_code=200)

@app.get("/")
def greet():
    return {"Hello":"World"}

@app.post("/plot_distribution")
def send_distribution(params: Plotparams):
    return generate_distribution(params)