from rest_framework import serializers

from exchange.serializers import CurrencySerializer


class CreateExchangeRatesRequestSerializer(serializers.Serializer):
    """
        Serializer for create request of exchange rate.
    """
    baseCurrencyCode = serializers.CharField(max_length=3)
    targetCurrencyCode = serializers.CharField(max_length=3)
    rate = serializers.FloatField()


class CreateExchangeRatesResponseSerializer(serializers.Serializer):
    """
        Serializer for create response of exchange rate.
    """
    baseCurrency = CurrencySerializer(source='base_currency')
    targetCurrency = CurrencySerializer(source='target_currency')
    rate = serializers.FloatField()


class GetExchangeRateRequestSerializer(serializers.Serializer):
    """
        Serializer for get request of exchange rate by currencies code pair.
    """
    code_pair = serializers.CharField(max_length=6)


class GetExchangeRateResponseSerializer(serializers.Serializer):
    """
        Serializer for get response of exchange rater.
    """
    baseCurrency = CurrencySerializer(source='base_currency')
    targetCurrency = CurrencySerializer(source='target_currency')
    rate = serializers.FloatField()


class UpdateExchangeRateRequestSerializer(serializers.Serializer):
    """
        Serializer for update request of exchange rate.
    """
    code_pair = serializers.CharField(max_length=6)
    rate = serializers.DecimalField(max_digits=100, decimal_places=28)


class UpdateExchangeRateResponseSerializer(serializers.Serializer):
    """
        Serializer for update response of exchange rate.
    """
    baseCurrency = CurrencySerializer(source='base_currency')
    targetCurrency = CurrencySerializer(source='target_currency')
    rate = serializers.FloatField()
