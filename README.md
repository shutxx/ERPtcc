# ERPtcc

## Back-end

### Instalação
- **Clone o repositório:** `git clone https://github.com/shutxx/ERPtcc.git`
- **Entre no diretório do projeto:** `cd ERPtcc`
- **Crie uma venv:** `python -m venv venv`
- **Inicie a venv:** `venv\Scripts\activate`
- **Instale as dependências:** `pip install -r requirements.txt`
### Aplique as migrações do banco de dados 
- **primeiro:** `python manage.py makemigrations` 
- **segundo:** `python manage.py migrate`
- **Subir servidor** `python manege.py runserver `