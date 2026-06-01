from django.db import IntegrityError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import CreateExchangeRateDTO
from exchange.repository import ExchangeRateRepository
from exchange.serializers import CreateExchangeRatesResponseSerializer, CreateExchangeRatesRequestSerializer
from exchange.services import ExchangeRateService


class ExchangeRatesView(APIView):

    def get(self, request: Request) -> Response:
        """
        Get all exchange rates.

        Args:
            request (Request): Contains request data.

        Returns:
            Response: Contains all found exchange rates.
        """
        exchange_rates = ExchangeRateRepository.get_all()
        serializer = CreateExchangeRatesResponseSerializer(exchange_rates, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        """
        Create exchange rate and return it.

        Args:
            request: Contains request data

        Returns:
            Response: Contains data of created exchange rate

        """
        request_serializer = CreateExchangeRatesRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        dto = CreateExchangeRateDTO(
            base_currency_code=request_serializer.data["baseCurrencyCode"],
            target_currency_code=request_serializer.data["targetCurrencyCode"],
            rate=request_serializer.data["rate"],
        )
        exchange_rate = ExchangeRateService.create_exchange_rate(dto)
        response_serializer = CreateExchangeRatesResponseSerializer(exchange_rate)
        return Response(response_serializer.data)


