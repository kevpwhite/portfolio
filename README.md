# Portfolio Code 

## Considerations

This code is for personal use. This is my portfolio code build on Django with tailwind.css and tailwind elements. This has been dockerized for easy migrations and flexability. 

## Prerequisite 

1. Built for linux debian flavors. Might work on other OS systems but I did not test it. 
2. Nginx proxy server used.
3. Let's Encrypt used.
4. Can be self hosted with the correct infrastructure or used on a cloud provider.
5. Environment Files Needed in root folder. Refer to example in code and change with your variables. All variables are set in the settings.py file for django.
    1. .env for development
    2. .env.prod for development

This will spin up 2 containers; django built in runserver and postgres container
```bash
# Create .env file
sudo nano .env 

DEBUG=1
SECRET_KEY=$SECRET_KEY

EMAIL_PASSWORD=$EMAIL_PASSWORD
EMAIL_ADMIN=$EMAIL_ADMIN
EMAIL_ADDRESS=$EMAIL_ADDRESS
EMAIL_PORT=$EMAIL_PORT
EMAIL_HOST=$EMAIL_HOST
EMAIL_USE_TLS=$EMAIL_USE_TLS

SQL_ENGINE=django.db.backends.postgresql
POSTGRES_DB=$POSTGRES_DB
POSTGRES_USER=$POSTGRES_USER
POSTGRES_PASSWORD=$POSTGRES_PASSWORD
SQL_HOST=$SQL_HOST
SQL_PORT=$SQL_POST
DATABASE=$DATABASE

ALLOWED_HOSTS=yourdomainname.com,www.yourdomainname.com
CSRF_TRUSTED_ORIGINS=https://*.yourdomainname.com,http://*.yourdomainname.com

# Set permissions for .env
sudo chmod 600 .env

# Command to build docker containers
sudo docker-compose up -d --build

#migrate database
sudo docker-compose exec web python3 manage.py migrate --noinput
```

## Production 

This has will spin up 3 containers; nginx, gunicorn, and postgres containers
```bash
# Create .env file
sudo nano .env 

#copy these variables and use the correct strings
DEBUG=1
SECRET_KEY=$SECRET_KEY

EMAIL_PASSWORD=$EMAIL_PASSWORD
EMAIL_ADMIN=$EMAIL_ADMIN
EMAIL_ADDRESS=$EMAIL_ADDRESS
EMAIL_PORT=$EMAIL_PORT
EMAIL_HOST=$EMAIL_HOST
EMAIL_USE_TLS=$EMAIL_USE_TLS

SQL_ENGINE=django.db.backends.postgresql
POSTGRES_DB=$POSTGRES_DB
POSTGRES_USER=$POSTGRES_USER
POSTGRES_PASSWORD=$POSTGRES_PASSWORD
SQL_HOST=$SQL_HOST
SQL_PORT=$SQL_POST
DATABASE=$DATABASE

ALLOWED_HOSTS=yourdomainname.com,www.yourdomainname.com
CSRF_TRUSTED_ORIGINS=https://*.yourdomainname.com,http://*.yourdomainname.com

# Set permissions for .env
sudo chmod 600 .env.prod

# Create SSL Certificate
cd nginx
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ./etc/ssl/private/localhost.key -out ./etc/ssl/certs/localhost.crt

# Command to build docker production containers
sudo docker-compose up -f docker-compose.prod.yml up -d --build

# Command to migrate all the django models 
sudo docker-compose -f docker-compose.prod.yml exec web python3 manage.py migrate

# Command to build all static files.
sudo docker-compose -f docker-compose.prod.yml exec web python3 manage.py collectstatic

```

# NOTES ARE NOT COMPLETED STILL A WORK IN PROGRESS....
