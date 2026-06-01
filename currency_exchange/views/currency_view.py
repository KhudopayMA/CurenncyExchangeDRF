from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from currency_exchange.models import Currency
from currency_exchange.repository import CurrencyRepository
from currency_exchange.serializers import CurrencySerializer


class CurrencyView(APIView):

    def get(self, request: Request, code: str) -> Response:
        """
        Get currency by code.
        Args:
            request (Response): Contains request data
            code (str): path parameter indicating the currency code

        Returns:
            Response: Contains data of found currency
        """
        currency = CurrencyRepository.get_by_code(code=code)
        serializer = CurrencySerializer(currency)
        return Response(serializer.data)



