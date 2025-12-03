from dotenv import load_dotenv
from pathlib import Path
import os

# Carpeta donde está este fichero
BASE_DIR = Path(__file__).resolve().parent
while not (BASE_DIR / ".env").exists() and BASE_DIR.parent != BASE_DIR:
    BASE_DIR = BASE_DIR.parent

# Cargar variables de entorno
load_dotenv(BASE_DIR / ".env")
