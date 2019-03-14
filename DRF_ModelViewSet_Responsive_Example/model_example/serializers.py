from custom_class.dynamic_field_serializer import DynamicFieldSerializer
from model_example.models import Book

class BookSerialzier(DynamicFieldSerializer):
	class Meta:
		model = Book
		fields = ('__all__')
