# speakapp
Share your thoughts, build a campaign and get supporters through Twitter!


#Actualizar aptitude
sudo apt-get update
sudo apt-get upgrade

#revisar version actual de python
python --version
#reemplazar version default por la 3 (incluir en .bashrc sino se reinicia con la sesion ssh) 
alias python=python3

#Instalar pip para python 3
sudo apt-get install python3-pip

#Hacer pip3 ejecutable al usar el comando "pip" (incluir en .bashrc sino se reinicia con la sesion ssh) 
alias pip=pip3

#Crear virtualenv y activarlo
virtualenv -p python3 miproyecto
source miproyecto/bin/activate

#Si no hay proyecto previo
pip install django

#Si hay proyecto previo (pip requirements)
#Instalar git
deactivate
sudo apt-get install git
#clonar proyecto
git clone https://rcamposp@bitbucket.org/rcamposp/speakapp.git speakapp

#Instalar pip requirements
source bin/activate
pip install -r requirements.txt

#Postgress python libraries
deactivate
sudo apt-get install libpq-dev python-dev
#Postgress server
sudo apt-get install postgresql postgresql-contrib

#Instalar NGINX
sudo apt-get install nginx

#Instalar GUNICORN
source bin/activate
pip install gunicorn
deactivate

#Configurar Postgress
sudo su - postgres
createdb mydb
createuser mydb_user -P
psql
GRANT ALL PRIVILEGES ON DATABASE mydb TO mydb_user;

#Instalar python adapter para Postgress 
source bin/activate

#Seguir paso 8: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn

#correr Gunicorn (en la misma carpeta del manage.py)
gunicorn speakapp.wsgi -b 159.203.87.92:8000

#Crear usuarios de sistema para que corran la aplicación
sudo groupadd --system webapps
sudo useradd --system --gid webapps --shell /bin/bash --home /home/apps speakapp

#gunicorn script para subir servidor dentro de /home/apps/django_env(virtualenv)/bin/gunicorn_dev_start(nombre_script)
#!/bin/bash

NAME="speakapp"
DJANGODIR=/home/speakapp/speakapp       # Django project directory
SOCKFILE=/home/speakapp/speakapp/gunicorn.sock  # we will communicte using this unix socket
PROXY=0.0.0.0:8001
VIRTUALENVDIR=/home/speakapp/django_env
USER=speakapp                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=speakapp.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=speakapp.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $VIRTUALENVDIR
source bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$VIRTUALENVDIR:$PYTHONPATH

# Create the run directory if it doesn't exist
#RUNDIR=$(dirname $SOCKFILE)
#test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
cd $DJANGODIR
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  -b=$PROXY \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --log-file=-

  ####################################################


#supervisor script
[program:speakapp]
command = /home/speakapp/django_env/bin/gunicorn_prod_start                    ; Command to start app
user = root                                                   ; User to run as
stdout_logfile =  /var/log/supervisor/supervisord.log   ; Where to write log messages
redirect_stderr = true                                                ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8                       ; Set UTF-8 as default encoding
