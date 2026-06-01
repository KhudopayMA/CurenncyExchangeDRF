from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView

from exchange.dto import CurrencyDto
from exchange.repository import CurrencyRepository
from exchange.serializers import CurrencySerializer


class CurrenciesView(APIView):

    def get(self, request: Request) -> Response:
        """
        Get all currencies.

        Args:
            request (Request): Contains request data.

        Returns:
            Response: Contains all found currencies.

        """
        currencies = CurrencyRepository.get_all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Create currency and return it.

        Args:
            request (Request): Contains request data

        Returns:
            Response: Contains data of created currency
        """
        request_serializer = CurrencySerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        currency_dto = CurrencyDto(**request_serializer.validated_data)
        currency = CurrencyRepository.create(currency_dto)
        response_serializer = CurrencySerializer(currency)
        return Response(response_serializer.data)



