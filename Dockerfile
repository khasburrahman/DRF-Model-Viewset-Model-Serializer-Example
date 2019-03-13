FROM python:3.6.8-alpine3.9

WORKDIR /usr/src/modelviewsetexample
COPY /DRF_ModelViewSet_Responsive_Example /usr/src/modelviewsetexample

RUN (pip install -r requirements.txt)
