from dataclasses import asdict

from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import ExchangeRateDto, GetRequestExchangeRateDto, CreateExchangeRateDTO, GetExchangeDto
from exchange.models import ExchangeRate, Currency
from exchange.repository import ExchangeRateRepository, CurrencyRepository
from exchange.serializers import ExchangeRatesRequestSerializer, ExchangeRatesResponseSerializer, \
    GetExchangeRequestSerializer, GetExchangeResponseSerializer
from exchange.services import ExchangeRateService, ExchangeService


class ExchangeView(APIView):

    def get(self, request):
        request_serializer = GetExchangeRequestSerializer(data=request.query_params)
        request_serializer.is_valid(raise_exception=True)
        dto = GetExchangeDto(**request_serializer.validated_data)
        exchange_dto = ExchangeService.get_exchange(dto)
        response_serializer = GetExchangeResponseSerializer(exchange_dto)
        return Response(response_serializer.data)
