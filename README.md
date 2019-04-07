# DRF Model Viewset Model Serializer Example

### To run the example for the first time:
Make sure you have python 3 installed, clone the repo and:  
- install the dependencies using `pip install -r requirements.txt`
- migrate the sqlite3 database `python manage.py migrate`
- start the service: `python manage.py runserver 0:8000`
- the app is served at localhost:8000, and you can browse the admin page at `/admin`

### Running the example for the next time
- start the service: `python manage.py runserver 0:8000`

This repo has a `docker flavor with postgresql` see the docker brach