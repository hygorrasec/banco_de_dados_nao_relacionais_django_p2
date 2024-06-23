# P2 DJANGO

### Comandos

 - Criando Ambiente Virtual: ```python -m venv venv```
 - Iniciando Ambiente Virtual (Linux): ```. venv/bin/activate```
 - Iniciando Ambiente Virtual (Windows PowerShell): ```.\venv\Scripts\Activate.ps1```
 - Iniciando Ambiente Virtual (Windows CMD): ```.\venv\Scripts\activate.bat```
 - Instalando bibliotecas: ```pip install -r requirements.txt```
 - Criando Superuser: ```python manage.py createsuperuser```
 - Makemigrations: ```python manage.py makemigrations```
 - Migrate: ```python manage.py migrate --run-syncdb```
 - Iniciar servidor: ```python manage.py runserver```

### Redis

 - (Windows) Instale o Redis que está na pasta raiz e acessar usando o Power Shell modo administrador: ```cd "C:\Program Files\Redis"```
 - Visualizar se existe algum processo sendo executado: ```netstat -aon | findstr 6379```
 - Se tiver e precisar finalizar, use o comando: ```taskkill /PID <PID> /F```
 - Verificar se finalizou: ```netstat -aon | findstr 6379```
 - Iniciar o Redis: ```.\redis-server.exe```
 - Iniciando servidor usando daphne: ```daphne -p 8000 p2_django.asgi:application```
