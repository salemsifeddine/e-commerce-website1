from rest_framework import serializers
from .models import *

class APISerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields="__all__"

class APISerializerCat(serializers.ModelSerializer):
    class Meta:
        model= CategoryList
        fields="__all__"