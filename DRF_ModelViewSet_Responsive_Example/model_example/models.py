from django.db import models
import uuid

# Create your models here.
class Example(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    fielda = models.CharField(max_length=50)
    fieldb = models.CharField(max_length=50)
    fieldc = models.CharField(max_length=50)