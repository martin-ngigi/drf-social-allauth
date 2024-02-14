## INSTALLATIONS
```
pip install django
pip install djangorestframework
pip install django-allauth
pip install django django-allauth
```

- Link: 
- [Github](https://www.youtube.com/watch?v=d7OxfJZOIhQ&t=10s)
- [Youtube](https://github.com/CryceTruly/incomeexpensesapi)

- Enable Google credentials
- [Link](https://console.cloud.google.com/apis/credentials/consent?project=social-authentiaction)

- Create Meta App for facebook
- [Link](https://developers.facebook.com/apps)

- Twitter
- [Link](https://developer.twitter.com/en/portal/apps)

- Run server
```
source .venv/bin/activate
cd project
python3 manage.py runserver
```

- Run migration
```
source .venv/bin/activate
cd project
python3 manage.py makemigrations
python3 manage.py migrate
```

# Using all Auth:
- Link to authenticate users
```
[Link](http://127.0.0.1:8000/accounts/signup/)
```

## NB:
- Dont forget to add "Authorized JavaScript origins" in [Link](https://console.cloud.google.com/apis/credentials/) 
```
http://127.0.0.1:8000
```
- Also add "Authorized redirect URI"s in google console
```
http://127.0.0.1:8000
http://127.0.0.1:8000/accounts/google/login/callback/
```

# LOGIN WITH ALLAUTH:
- URL : http://127.0.0.1:8000/accounts/login/