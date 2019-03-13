from django.shortcuts import render
from rest_framework import viewsets
from model_example.serializers import ExampleSerialzier
from model_example.models import Example

class ExampleViewSet(viewsets.ModelViewSet):
    serializer_class = ExampleSerialzier
    queryset = Example.objects.all()


