from rest_framework import serializers


class CurrencySerializer(serializers.Serializer):
    """
        Serializer for object of Currency model
    """
    id = serializers.BigIntegerField(read_only=True)
    code = serializers.CharField(max_length=3)
    name = serializers.CharField(max_length=100)
    sign = serializers.CharField(max_length=3)
