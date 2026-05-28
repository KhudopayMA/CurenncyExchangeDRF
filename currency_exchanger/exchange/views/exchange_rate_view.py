from django.db import IntegrityError
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import ExchangeRateDto, RequestExchangeRateDto, CreateExchangeRateDTO
from exchange.models import ExchangeRate, Currency
from exchange.repository import ExchangeRateRepository, CurrencyRepository
from exchange.serializers import ExchangeRatesRequestSerializer, ExchangeRatesResponseSerializer, ExchangeRateRequestSerializer
from exchange.services import ExchangeRateService




class ExchangeRateView(APIView):

    def get(self, request: Request, code_pair: str):
        request_serializer = ExchangeRateRequestSerializer(data={"code_pair": code_pair})
        request_serializer.is_valid(raise_exception=True)
        exchange_rate = ExchangeRateService.get_exchange_rate(request_serializer.validated_data["code_pair"])
        response_serializer = ExchangeRatesResponseSerializer(exchange_rate)
        return Response(response_serializer.data)

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


