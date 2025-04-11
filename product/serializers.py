from rest_framework import serializers
from .models import Noutbooks

class NoutbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noutbooks
        fields = '__all__'
