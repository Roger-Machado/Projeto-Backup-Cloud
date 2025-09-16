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
