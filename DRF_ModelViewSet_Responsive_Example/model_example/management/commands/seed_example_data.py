from django.core.management.base import BaseCommand, CommandError
from model_example.models import Book

class Command(BaseCommand):
    def handle(self, *args, **options):
        '''
        0 => title
        1 => author
        2 => isbn
        3 => price
        4 => synopsis
        '''

        bookList = [
            ['Fundamentals of Wavelets', 'Goswami, Jaideva', '1234567890123', '322000', 'Synopsis sample'],
            ['Data Smart', 'Foreman, John', '1234567890123', '322000', 'Synopsis sample'],
            ['God Created the Integers', 'Hawking, Stephen', '1234567890123', '322000', 'Synopsis sample'],
        ]

        for book in bookList: 
            Book.objects.get_or_create(
                title=book[0], author=book[1], isbn=book[2], 
                price=book[3], synopsis=book[4])