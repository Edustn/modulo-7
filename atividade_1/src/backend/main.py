from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
from modelo import executar_modelo
import re

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

@app.get("/executar/modelo")
def modelo():
    resultado = executar_modelo()
    soma = 0
    message = ""
    certo = 0
    message_certo = ""
    tamanho = resultado[1].split(" ")
    for i in range(len(tamanho)):
        # print(resultado[1][i])
        print(tamanho[i])
        if tamanho[i].strip().__contains__('False'):
            soma +=1 
        elif tamanho[i].strip().__contains__('True'):
            message_certo += tamanho[i] + " "
        
    if soma > 3:
        message += "Essa semana não indico você não comprar nenhum Bitcoin"

    else:
            message = f"Essa semana me parece boa para comprar Bitcoins, compre nos seguintes dias {message_certo}"    
   
    date_pattern =  r'\d{4}-\d{2}-\d{2}'
    dates = re.findall(date_pattern, resultado[0])
    print(dates)

    return [message, dates]

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)