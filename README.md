# Todo-API

World needs more todo-apps :)  
This one is a Django / Django REST Framework powered todo-API.  
Vue.js frontend is coming later...

Basic idea is that there can be several users.  
Users have their own todo-lists and users have to authenticate.  
Authentication and registering new users can be made through API.  
Items in todo-list can be created, read, updated and destroyed (CRUD).  
Items have status for done / not done.   
Items have an order in list and they can be re-ordered with API.  

Note that currently this is just the start of the project so Django is only set up for development! It also uses SQLite as database and a populated database file is in the repository for easy start. 
If you want to 'start fresh', just delete db.sqlite3 database file and run `python manage.py migrate` to re-create it.  
Then create superuser with `python manage.py createsuperuser`.  

Database username / password:  
superuser / testpassSU  (Django admin)  
user1 / testpassU1  
user2 / testpassU2  
user3 / testpassU3

#### Get started

Clone the repository  
After that you have two choises:  
1. Docker  
2. Traditional Python way


##### 1. Docker

Install Docker and docker-compose  
Run `docker-compose up` at project root (where docker-compose.yml is)  
(make sure your user has proper rights to docker or use `sudo`)

##### 2. Traditional Python way

Use virtual environment of your choice, but with pipenv:  
Change directory to /backend: `cd backend`    
Install dependencies: `pipenv install --dev`  
Activate virtual environment: `pipenv shell`  
Run Django development server: `python manage.py runserver`

Either way, you should now have Django running at http://127.0.0.1:8000  
and Django admin at http://127.0.0.1:8000/admin  

API endpoints (and DRF browsable UI) are at http://127.0.0.1:8000/api/v1/  
For example: (see Swagger below for all endpoints)  
- List users todos: /v1/
- Get single todo: /v1/{todo-id}/
- Re-order todo: /v1/{todo-id}/order/  
(POST request with new order number in request body)
- Login with API: /v1/dj-rest-auth/login/
- Logout with API: /v1/dj-rest-auth/logout/
- Register new user with API: /v1/dj-rest-auth/registration/  
(+ all other dj-rest-auth endpoints for password reset, reset and registration confirm: check /v1/swagger/) 
- Swagger: /v1/swagger/
- Swagger JSON: /v1/swagger.json
- Redoc: /v1/redoc/


##### Thanks!
Ordering logic is heavily inspired by https://www.revsys.com/tidbits/keeping-django-model-objects-ordered/. Thank you for inspiration!  
And thank you for all involved in projects listed in Pipfile!