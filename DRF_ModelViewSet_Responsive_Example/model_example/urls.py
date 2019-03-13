from rest_framework import routers
from model_example.views import ExampleViewSet

router = routers.SimpleRouter()

router.register(r'example', ExampleViewSet)
urlpatterns = router.urls