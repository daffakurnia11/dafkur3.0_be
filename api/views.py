from rest_framework import generics
from .models import ContactModel
from .serializers import ContactSerializer


class ContactViewSet(generics.CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
