from rest_framework import serializers

from exchange.serializers import CurrencySerializer


class ExchangeRateCreateSerializer(serializers.Serializer):
    baseCurrencyCode = serializers.CharField(max_length=3)
    targetCurrencyCode = serializers.CharField(max_length=3)
    rate = serializers.FloatField()


class ExchangeRateResponseSerializer(serializers.Serializer):
    baseCurrency = CurrencySerializer(source='base_currency')
    targetCurrency = CurrencySerializer(source='target_currency')
    rate = serializers.FloatField()
