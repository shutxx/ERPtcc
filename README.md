# ERPtcc
## Back-end
### Instalação
- **Clone o repositório:** `git clone https://github.com/shutxx/ERPtcc.git`
- **Entre no diretório do projeto:** `cd ERPtcc`
- **Entre na pasta do back-end:** `cd back-end`
- **Crie seu ambiente virtual:** `python -m venv venv`
- **Inicie a venv:** `venv\Scripts\activate`
- **Instale as dependências:** `pip install -r requirements.txt`
- **Subir servidor** `python manege.py runserver `
    #### Após subir o servidor, o banco de dados sqlite sera criado, so aplicar a migração 

### Aplique as migrações do banco de dados 
- **Pare o servidor e aplique:** `python manage.py migrate`
- **Servidor vai subir em:** `http://127.0.0.1:8000/`