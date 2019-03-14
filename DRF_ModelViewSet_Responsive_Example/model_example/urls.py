from rest_framework import routers
from model_example.views import BookViewSet

router = routers.SimpleRouter()

router.register(r'book', BookViewSet)
urlpatterns = router.urls