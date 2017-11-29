# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .serializers import risk_type_Serializer
from .serializers import risk_type_fields_Serializer
from .models import risk_type
from .models import risk_type_fields

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = risk_type.objects.all()
    serializer_class = risk_type_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new risk_type."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = risk_type.objects.all()
    serializer_class = risk_type_Serializer

class CreateFieldView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = risk_type_fields.objects.all()
    serializer_class = risk_type_fields_Serializer

    def perform_create(self, serializer):
        """Save the post data when creating a new risk_type_fields."""
        serializer.save()

class FieldListView(generics.ListAPIView):
    serializer_class = risk_type_fields_Serializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        type_id = self.kwargs['id']
        return risk_type_fields.objects.filter(risk_type_id=type_id)



    


