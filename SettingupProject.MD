# Setting up the environment on Mac
- Create a directory  and navigate to directory
```
 mkdir drf-social-allauth
 cd drf-social-allauth
```
- create a virtual environment and activate it
```
python3 -m venv .venv
source .venv/bin/activate
```
- Install pip and django
```
 python3 -m pip install --upgrade pip
 python3 -m pip install django
```
- Start project and navigate to directory
```
django-admin startproject project
```
- Run server
```
source .venv/bin/activate
cd project
python3 manage.py runserver
```
- Create apps
```
python3 manage.py startapp authentication
python3 manage.py startapp profile_account
```

- Create super admin
```
python3 manage.py createsuperuser
```