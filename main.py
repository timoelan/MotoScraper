from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_tutti_data():
    """Lädt die Daten aus der JSON-Datei und gibt sie zurück."""
    file_path = "scraper/tutti/tutti_anzeigen.json"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="JSON-Datei nicht gefunden")
    
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

@app.get("/tutti-content")
def get_tutti_content():
    """Gibt die neuesten Daten aus der JSON-Datei zurück."""
    try:
        tutti_data = load_tutti_data()
        return tutti_data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fehler beim Laden der Daten: {str(e)}")