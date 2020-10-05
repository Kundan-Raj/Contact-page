from rest_framework import serializers
from test1.models import Contactdb

class contactserializer(serializers.ModelSerializer):
    class Meta:
        model= Contactdb
        fields= ("__all__")