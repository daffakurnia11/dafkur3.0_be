from rest_framework import viewsets
from .models import ContactModel
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
