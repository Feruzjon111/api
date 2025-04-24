from rest_framework import serializers
from product.models.models import Noutbooks

class NoutbooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noutbooks
        fields = '__all__'
