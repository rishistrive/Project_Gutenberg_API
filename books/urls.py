from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    # Include the router URLs
    path('', include(router.urls)),
]
