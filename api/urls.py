from django.urls import path
from .views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path("contact/", ContactViewSet.as_view(), name="contact-create"),
    # Other URL patterns if any
]
