from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil

import uvicorn

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIRECTORY = BASE_DIR / "database"  # Caminho relativo ao diretório do script

app.add_middleware ( 
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:7000"]

)


@app.get("/hello")
def principal():
    return "Hello, World!"

@app.post("/inserirBase")
async def inserir_base(file: UploadFile = File(...)):
    file_location = UPLOAD_DIRECTORY / file.filename

    # Salvando o arquivo na pasta especificada
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"info": f"Arquivo '{file.filename}' salvo com sucesso em {file_location}"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)