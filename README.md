# DRFPostgresDocker
this example is using docker, install docker and docker-compose first before using it

### Docker volume mounting
I'm using docker in virtual box, if you happen to have the same setup: add the `DRF_ModelViewSet_Responsive_Example` folder to virtualbox shared folder with the same name. If you're not using virtualbox IIRC: add a dot before the mounting point 

in docker-compose.yml
```
volumes:
      - ./DRF_ModelViewSet_Responsive_Example:/usr/src/modelviewsetexample
```
in Dockerfile 
```
COPY /DRF_ModelViewSet_Responsive_Example /usr/src/modelviewsetexample
```

### Allowed hosts
- If you're using docker desktop without virtual box, skip this
- If you're using virtual box, run `docker-machine ip` and put the ip to the `App\settings.py`
```
ALLOWED_HOSTS = ['<<your docker machine ip here>>', 'localhost']
```

### To run the example for the first time: 
1. clone the repo, cd inside to the repo directory and do:  
      - build the `pythonexample` image: `docker-compose build`
      - start the service: `docker-compose up`
2. open a new terminal, start the docker interactive container shell: `docker exec -it pythonexample sh`
      - migrate the database: `python manage.py migrate`
      - run the seed command `python manage.py seed_example_data`
      - (optional) for login to the django admin page:`<<app-ip>>/admin` create super user: `python manage.py createsuperuser` and follows the instruction

### Running the example for the next time
1. just start the service, cd to the repo directory and `docker-compose up`
