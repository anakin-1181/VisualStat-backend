from fastapi import FastAPI
from app.core.distribution import generate_distribution
from app.models.model import Plotparams

app = FastAPI()

@app.get("/")
def greet():
    return {"Hello":"World"}

@app.post("/plot_distribution")
def send_distribution(params: Plotparams):
    return generate_distribution(params)