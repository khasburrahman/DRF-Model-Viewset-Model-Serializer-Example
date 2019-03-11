# DjangoModelViewSetExample
this example is using docker, install docker and docker-compose first before using it

### Docker volume
I'm using docker in virtual box, if you happen to have the same setup: add the `DRF_ModelViewSet_Responsive_Example` folder to virtualbox shared folder with the same name. If you're not using virtualbox IIRC: add a dot before the mounting point 

```
volumes:
      - ./DRF_ModelViewSet_Responsive_Example:/usr/src/modelviewsetexample
```

### To run the example: 
1. clone the repo
2. in the cloned directory do `docker-compose up`
3. the app will be up in `localhost:8000`
