from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    synopsis = models.TextField()