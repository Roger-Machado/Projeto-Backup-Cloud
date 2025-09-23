import os
import subprocess
from datetime import datetime
from dotenv import load_dotenv

# ================= CONFIGURAÇÕES =================
load_dotenv()

LOCAL_DIR = os.getenv("LOCAL_DIR")
AWS_BUCKET = os.getenv("AWS_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")

# Função de log
def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

# Função de backup para AWS S3
def backup_aws():
    try:
        log(f"Iniciando upload AWS S3: {LOCAL_DIR} -> s3://{AWS_BUCKET}/")
        cmd = [
            "aws", "s3", "sync",
            LOCAL_DIR,
            f"s3://{AWS_BUCKET}/",
            "--region", AWS_REGION,
            "--acl", "private",
        ]
        subprocess.run(cmd, check=True)
        log("Upload concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        log(f"Erro no upload: {e}")

# Loop para enviar todos os arquivos da pasta
def main():
    backup_aws()

if __name__ == "__main__":
    main()
