FROM python:3.6.8-alpine3.9

WORKDIR /usr/src/modelviewsetexample

COPY ./DRF_ModelViewSet_Responsive_Example/requirements.txt .

RUN \
    apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    python3 -m pip install -r requirements.txt --no-cache-dir && \
    apk --purge del .build-deps

COPY ./DRF_ModelViewSet_Responsive_Example /usr/src/modelviewsetexample

CMD [ "python manage.py runserver 0:8000" ]
