# Projeto-Backup-Cloud

# 🗂️ Script de Backup Local e AWS S3

Este projeto contém um script em **Python** que automatiza o processo de backup de arquivos locais.  
Ele faz duas etapas principais:

1. **Backup Local** → copia os arquivos de um diretório configurado para uma pasta de backup no computador.  
2. **Upload para AWS S3** → envia os mesmos arquivos para um bucket no Amazon S3, mantendo versionamento via metadados.  

---

## ⚙️ Tecnologias utilizadas
- Python 3.x  
- AWS CLI  
- Bibliotecas padrão do Python (`os`, `shutil`, `subprocess`, `datetime`)  

---

## 📂 Estrutura do projeto
│ <br />
├─ arquivos/ # Pasta com os arquivos que serão enviados para o S3 <br />
│ └─ teste_arquivo.txt # Arquivo de exemplo <br />
├─ backup_cloud.py # Script principal de backup <br />
├─ .env.example # Arquivo de configuração de variáveis de ambiente <br />
└─ README.md # Documentação do projeto <br />


## ⚙️ Configuração do ambiente
**1. Procure pelo arquivo .env.example**
```
Renomear ele para >>> .env
```

**2. Configure as seguintes variáveis de ambiente com os valores seguindo a descrição de cada uma delas**
```bash
LOCAL_DIR= # Diretório local dos arquivos a serem enviados para o S3
AWS_BUCKET= # Nome do bucket S3
AWS_REGION= # Região do bucket S3
```

**3. Instale a dependência relacioanada ao dotenv**
```
pip install python-dotenv
```

**4. Configure o AWS CLI com seu usuário IAM que possui acesso ao Bucket**
```
aws configure
```
Ao executar o comando, ele pedirá algumas credências para acessar o serviço da AWS, sendo elas:
```bash
- AWS Access Key ID: # Chave do usuário IAM
- AWS Secret Access Key: # Chave secreta do usuário IAM
- Default region name: # Região do Bucket
- Default output format: # Formato de saída padrão (podendo ser 'json' ou podendo deixar em branco)
```

**5. Por fim, execute o seguinte comando para upar os arquivos presentes na pasta `arquivos`**
```
python backup_cloud.py
```