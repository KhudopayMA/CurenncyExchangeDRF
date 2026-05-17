from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import ValidationError, APIException
from rest_framework.validators import UniqueValidator

from .models import Currency, ExchangeRate

class CurrencyCodeAlreadyExist(APIException):
    status_code = status.HTTP_409_CONFLICT

class CurrenciesSerializer(serializers.Serializer):

    code = serializers.CharField(max_length=3)
    name = serializers.CharField(max_length=100)
    sign = serializers.CharField(max_length=3)

    def create(self, validated_data):
        return Currency.objects.create(**validated_data)

    def validate_code(self, data):
        if Currency.objects.filter(code=data).exists():
            raise CurrencyCodeAlreadyExist(detail=f"Currency {data} already exists")
        return data

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class ExchangeRatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExchangeRate
        fields = '__all__'

