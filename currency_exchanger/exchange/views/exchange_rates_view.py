from django.db import IntegrityError
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import ExchangeRateDto, RequestExchangeRateDto
from exchange.models import ExchangeRate, Currency
from exchange.repository import ExchangeRateRepository, CurrencyRepository
from exchange.serializers import ExchangeRateSerializer



class ExchangeRatesView(APIView):
    serializer_class = ExchangeRateSerializer
    exchange_rate_repository = ExchangeRateRepository()
    currency_repository = CurrencyRepository()

    def get(self, request: Request):
        exchange_rates = self.exchange_rate_repository.get_all()
        serializer = self.serializer_class(exchange_rates, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        request_serializer = self.serializer_class(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        base_currency = self.currency_repository.get(
            code=request_serializer.validated_data['baseCurrencyCode']
        )
        target_currency = self.currency_repository.get(
            code=request_serializer.validated_data['targetCurrencyCode']
        )
        try:
            exchange_rate_dto = ExchangeRateDto(
                base_currency = base_currency,
                target_currency = target_currency,
                rate=request_serializer.validated_data['rate'],
            )
            exchange_rate = self.exchange_rate_repository.create(exchange_rate_dto)
            response_serializer = self.serializer_class(exchange_rate)
            return Response(response_serializer.data)
        except IntegrityError as e:
            error_msg = str(e)
            if "UNIQUE constraint failed" in error_msg:
                filed = error_msg.split(".")[-1]
                return Response(
                    f"Field {filed} with value {request_serializer.validated_data.get(filed)} already exists.",
                    status=status.HTTP_409_CONFLICT,
                )


