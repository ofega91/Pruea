import os
from dotenv import load_dotenv

load_dotenv()
nombre = os.getenv("NOMBRE", "Desconocido")
print(f"Hola, mi nombre es {nombre}")