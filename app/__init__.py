from  fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# solve Access-Control-Allow-Origin
origins = [
    "*",
    "https://d12d-186-118-197-22.ngrok.io/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
    max_age=3600,
)

from app import views 