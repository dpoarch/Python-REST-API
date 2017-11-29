from rest_framework import serializers
from .models import risk_type
from .models import risk_type_fields

class risk_type_Serializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = risk_type
        fields = ('id','name')


class risk_type_fields_Serializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = risk_type_fields
        fields = ('risk_type_id', 'fieldname', 'fieldtype')