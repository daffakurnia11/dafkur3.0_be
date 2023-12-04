from django.urls import path, include
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"contact", ContactViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # Other URL patterns if any
]
