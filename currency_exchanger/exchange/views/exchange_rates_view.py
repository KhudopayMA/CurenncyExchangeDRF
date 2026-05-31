from django.db import IntegrityError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import ExchangeRateDto, GetRequestExchangeRateDto, CreateExchangeRateDTO
from exchange.models import ExchangeRate, Currency
from exchange.repository import ExchangeRateRepository, CurrencyRepository
from exchange.serializers import ExchangeRatesRequestSerializer, ExchangeRatesResponseSerializer
from exchange.services import ExchangeRateService




class ExchangeRatesView(APIView):

    def get(self, request: Request):
        exchange_rates = ExchangeRateRepository.get_all()
        serializer = ExchangeRatesResponseSerializer(exchange_rates, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        request_serializer = ExchangeRatesRequestSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        dto = CreateExchangeRateDTO(
            base_currency_code=request_serializer.data["baseCurrencyCode"],
            target_currency_code=request_serializer.data["targetCurrencyCode"],
            rate=request_serializer.data["rate"],
        )
        exchange_rate = ExchangeRateService.create_exchange_rate(dto)
        response_serializer = ExchangeRatesResponseSerializer(exchange_rate)
        return Response(response_serializer.data)


