from django.shortcuts import render
from rest_framework import viewsets
from model_example.serializers import BookSerialzier
from model_example.models import Book

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerialzier
    queryset = Book.objects.all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        action = self.action
        if (action == 'list'):
            context['fields'] = ('id', 'title', 'price',)
        elif (action == 'create'):
            context['fields'] = ('id',)
        elif (action == 'retrieve'):
            context['fields'] = ('title', 'author', 'isbn', 'price', 'synopsis')
        return context


