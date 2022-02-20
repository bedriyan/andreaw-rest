# Andreaw Rest 

This API is currently running on a Heroku server # https://andrew-backend-django.herokuapp.com/ 

API Documentation is available at https://documenter.getpostman.com/view/10807503/UVkjwxqk

React Native Repo is available at https://documenter.getpostman.com/view/10807503/UVkjwxqk


### [Running the project at the local machine](#virtualenv)

1. Clone the repository

```
  git clone https://github.com/bedriyan/andreaw-rest
```

3. Changing to project directory and creating Virtual Python Environment named `venv`

```
  cd andreaw-rest
  python3 -m venv venv
```

4. Activating the virtual environment

```
  source venv/bin/activate
```

5. Installing project dependencies

```
  pip install -r requirements.txt
```

6. Migrating the database 

```
  python manage.py makemigrations
  python manage.py migrate
```

7. Running the server

```
  python manage.py runserver
```





