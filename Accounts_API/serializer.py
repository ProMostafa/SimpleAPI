from rest_framework import serializers
from .models import Account , ClintOrder

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model=Account
        fields='__all__'


class ClientOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=ClintOrder
        fields='__all__'
