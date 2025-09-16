import os
import subprocess
from datetime import datetime

# ================= CONFIGURAÇÕES =================
LOCAL_DIR = r"C:\Programas\Projeto-Python\arquivos"  # Diretório local com arquivos
AWS_BUCKET = "meu-bucket-aws"  # Substitua pelo seu bucket
AWS_REGION = "us-east-1"       # Região do bucket

# Função de log
def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

# Função de backup para AWS S3
def backup_aws(file_path):
    try:
        log(f"Iniciando upload AWS S3: {file_path}")
        cmd = [
            "aws", "s3", "cp", file_path,
            f"s3://{AWS_BUCKET}/",
            "--region", AWS_REGION,
            "--acl", "private",
            "--metadata", f"version={datetime.now().isoformat()}"
        ]
        subprocess.run(cmd, check=True)
        log("Upload concluído com sucesso!")
    except subprocess.CalledProcessError as e:
        log(f"Erro no upload: {e}")

# Loop para enviar todos os arquivos da pasta
def main():
    for root, dirs, files in os.walk(LOCAL_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            backup_aws(file_path)

if __name__ == "__main__":
    main()
