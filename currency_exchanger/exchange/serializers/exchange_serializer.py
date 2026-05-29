from copy import copy

from rest_framework import serializers

from exchange.serializers import CurrencySerializer


class GetExchangeRequestSerializer(serializers.Serializer):
    from_currency_code = serializers.CharField(max_length=3)
    to_currency_code = serializers.CharField(max_length=3)
    amount = serializers.DecimalField(max_digits=100, decimal_places=28)

    def to_internal_value(self, data):
        transformed_data = dict(copy(data))
        request_to_serialized_fields_pairs = {"from": "from_currency_code", "to": "to_currency_code"}
        for field in data:
            if field in request_to_serialized_fields_pairs.keys():
                transformed_data[request_to_serialized_fields_pairs[field]] = transformed_data.pop(field)[0]
            else:
                transformed_data[field] = transformed_data[field][0]

        return super().to_internal_value(transformed_data)


class GetExchangeResponseSerializer(serializers.Serializer):
    baseCurrency = CurrencySerializer(source='base_currency')
    targetCurrency = CurrencySerializer(source='target_currency')
    rate = serializers.FloatField()
    amount = serializers.FloatField()
    convertedAmount = serializers.FloatField(source="converted_amount")

