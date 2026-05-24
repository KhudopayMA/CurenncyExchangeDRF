from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.models import Currency
from exchange.repository import CurrencyRepository
from exchange.serializers import CurrencySerializer


class CurrencyView(APIView):
    serializer_class = CurrencySerializer
    currency_repository = CurrencyRepository()

    def get(self, request, code):
        try:
            currency = self.currency_repository.get_currency(code=code)
        except Currency.DoesNotExist:
            return Response(f"Currency with code {code} not found",status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(currency)
        return Response(serializer.data)



