from rest_framework import serializers

from exchange.serializers import CurrencySerializer


class ExchangeRateSerializer(serializers.Serializer):
    baseCurrencyCode = serializers.CharField(max_length=3, write_only=True)
    targetCurrencyCode = serializers.CharField(max_length=3, write_only=True)

    baseCurrency = CurrencySerializer(source="base_currency", read_only=True)
    targetCurrency = CurrencySerializer(source="target_currency", read_only=True)

    rate = serializers.FloatField()
