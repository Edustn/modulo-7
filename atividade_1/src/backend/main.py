from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import shutil
import logging
import re
import uvicorn
from modelo import executar_modelo
import psycopg2
from datetime import datetime

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIRECTORY = BASE_DIR / "database"  # Caminho relativo ao diretório do script

# Função para conectar ao banco de dados PostgreSQL
def connect_db():
    conn = psycopg2.connect(
        dbname="eu_banco",
        user="usuario",
        password="senha",
        host="localhost",
        port="5432"
    )
    return conn

# Função para salvar logs no PostgreSQL
def save_log_to_db(log_level, message):
    conn = connect_db()
    cursor = conn.cursor()
    query = """INSERT INTO system_logs (log_level, message, timestamp) 
               VALUES (%s, %s, %s);"""
    cursor.execute(query, (log_level, message, datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()

# Criando um handler personalizado para o banco de dados
class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        save_log_to_db(record.levelname, log_entry)

# Configurar logging para salvar diretamente no banco de dados
db_handler = DatabaseLogHandler()
db_handler.setLevel(logging.INFO)

# Formato de log
formatter = logging.Formatter("%(message)s")
db_handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(db_handler)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=["http://localhost:7000"]
)

@app.get("/hello")
def principal():
    logger.info("Rota /hello acessada")
    return "Hello, World!"

@app.post("/inserirBase")
async def inserir_base(file: UploadFile = File(...)):
    file_location = UPLOAD_DIRECTORY / file.filename

    # Salvando o arquivo na pasta especificada
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    logger.info(f"Arquivo '{file.filename}' salvo em {file_location}")
    return {"info": f"Arquivo '{file.filename}' salvo com sucesso em {file_location}"}

@app.get("/executar/modelo")
def modelo():
    logger.info("Executando modelo")
    resultado = executar_modelo()
    soma = 0
    message = ""
    certo = 0
    message_certo = ""
    tamanho = resultado[1].split(" ")
    for i in range(len(tamanho)):
        print(tamanho[i])
        if tamanho[i].strip().__contains__('False'):
            soma += 1
        elif tamanho[i].strip().__contains__('True'):
            message_certo += tamanho[i] + " "

    if soma > 3:
        message += "Essa semana não indico você não comprar nenhum Bitcoin"
    else:
        message = f"Essa semana me parece boa para comprar Bitcoins, compre nos seguintes dias {message_certo}"

    date_pattern = r'\d{4}-\d{2}-\d{2}'
    dates = re.findall(date_pattern, resultado[0])
    logger.info(f"Datas encontradas: {dates}")

    return [message, dates]

@app.get("/logs")
async def get_logs():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT log_level, message, timestamp FROM system_logs ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    cursor.close()
    conn.close()

    return {"logs": logs}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
