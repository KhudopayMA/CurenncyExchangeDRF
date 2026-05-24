from rest_framework import serializers

from exchange.serializers import CurrencySerializer


class ExchangeRateSerializer(serializers.Serializer):
    baseCurrencyCode = serializers.CharField(max_length=3, write_only=True)
    targetCurrencyCode = serializers.CharField(max_length=3, write_only=True)

    base_currency = CurrencySerializer(read_only=True)
    target_currency = CurrencySerializer(read_only=True)

    rate = serializers.FloatField()