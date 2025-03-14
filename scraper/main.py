from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("tutti/tutti_anzeigen.json", "r", encoding="utf-8") as file:
    tutti_data = json.load(file)


@app.get("/tutti-content")
def get_tutti_content():
    return tutti_data
