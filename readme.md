# Django Starter Project

##### This project packed with custom User model, user register, login, logout, profile, update profile.

### **Get Started**

Clone Repository with git bash

```
git clone https://github.com/code-anwarhosen/django-starter.git
```

Move to the project dir

```
cd django-starter
```

Create a virtualenv and activate. (make sure you have python and python venv module)

```
python -m venv venv
.\venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run migrations

```
python manage.py makemigrations user
python manage.py migrate
```

You can also create superuser using `python manage.py createsuperuser` if you want to login to /admin.

Runserver

```
python manage.py runserver
```

Finally...

Now you can access

[http://127.0.0.1:8000/user/login/](http://127.0.0.1:8000/user/login/)

[http://127.0.0.1:8000/user/register/](http://127.0.0.1:8000/user/register/)

[http://127.0.0.1:8000/user/password-reset/](http://127.0.0.1:8000/user/password-reset/)

[http://127.0.0.1:8000/user/profile/](http://127.0.0.1:8000/user/profile/)

[http://127.0.0.1:8000/user/profile/update/](http://127.0.0.1:8000/user/profile/update/)

and more...

[GitHub: code-anwarhosen](https://github.com/code-anwarhosen)
