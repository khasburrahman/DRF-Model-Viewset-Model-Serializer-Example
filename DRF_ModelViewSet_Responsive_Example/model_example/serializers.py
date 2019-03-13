from custom_class.dynamic_field_serializer import DynamicFieldSerializer
from model_example.models import Example

class ExampleSerialzier(DynamicFieldSerializer):
	class Meta:
		model = Example
		fields = ('__all__')
