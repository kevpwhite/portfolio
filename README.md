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
    3. .env.prod.db for development database

This will spin up 2 containers; django built in runserver and postgres containers
```bash
# Create .env file
sudo nano .env 

EMAIL_PASSWORD=$EMAIL_PASSWORD
EMAIL_ADMIN=$EMAIL_ADMIN
EMAIL_ADDRESS=$EMAIL_ADDRESS
DEBUG=0
SECRET_KEY=$SECRET_KEY
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=$SQL_DATABASE
SQL_USER=$SQL_USER
SQL_PASSWORD=$SQL_PASSWORD
SQL_HOST=$SQL_HOST
SQL_PORT=$SQL_PORT
DATABASE=$DATABASE
#save to .env

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
EMAIL_PASSWORD=$EMAIL_PASSWORD
EMAIL_ADMIN=$EMAIL_ADMIN
EMAIL_ADDRESS=$EMAIL_ADDRESS
DEBUG=0
SECRET_KEY=$SECRET_KEY
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=$SQL_DATABASE
SQL_USER=$SQL_USER
SQL_PASSWORD=$SQL_PASSWORD
SQL_HOST=$SQL_HOST
SQL_PORT=$SQL_PORT
DATABASE=$DATABASE

# Create .env file
sudo nano .env.prod.db

#copy these variables and use the correct strings
POSTGRES_USER=$POSTGRES_USER
POSTGRES_PASSWORD=$POSTGRES_PASSWORD
POSTGRES_DB=$POSTGRES_DB

# Set permissions for .env
sudo chmod 600 .env.prod
sudo chmod 600 .env.prod.db

# Command to build docker production containers
sudo docker-compose up -f docker-compose.prod.yml up -d --build

# Command to migrate all the django models 
sudo docker-compose -f docker-compose.prod.yml exec web python3 manage.py migrate

# Command to build all static files.
sudo docker-compose -f docker-compose.prod.yml exec web python3 manage.py collectstatic

```

# NOTES ARE NOT COMPLETED STILL A WORK IN PROGRESS....
