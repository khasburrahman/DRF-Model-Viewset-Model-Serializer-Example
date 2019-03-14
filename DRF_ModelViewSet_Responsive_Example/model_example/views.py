from django.shortcuts import render
from rest_framework import viewsets
from model_example.serializers import BookSerialzier
from model_example.models import Book

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerialzier
    queryset = Book.objects.all()


