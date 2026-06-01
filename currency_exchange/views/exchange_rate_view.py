from django.db import IntegrityError
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from currency_exchange.dto import ExchangeRateDto, GetRequestExchangeRateDto, CreateExchangeRateDTO, UpdateExchangeRateDTO
from currency_exchange.models import ExchangeRate, Currency
from currency_exchange.repository import ExchangeRateRepository, CurrencyRepository
from currency_exchange.serializers import CreateExchangeRatesRequestSerializer, CreateExchangeRatesResponseSerializer, \
    GetExchangeRateRequestSerializer, UpdateExchangeRateRequestSerializer, GetExchangeRateResponseSerializer, \
    UpdateExchangeRateResponseSerializer
from currency_exchange.services import ExchangeRateService


class ExchangeRateView(APIView):

    def get(self, request: Request, code_pair: str) -> Response:
        """
        Get exchange rate by code pair.

        Args:
            request (Request): Contains request data
            code_pair (str): path parameter indicating the currencies code pair
        Returns:
            Response: Contains data of found exchange rate
        """
        request_serializer = GetExchangeRateRequestSerializer(data={"code_pair": code_pair})
        request_serializer.is_valid(raise_exception=True)
        exchange_rate = ExchangeRateService.get_exchange_rate(request_serializer.validated_data["code_pair"])
        response_serializer = GetExchangeRateResponseSerializer(exchange_rate)
        return Response(response_serializer.data)

    def patch(self, request: Request, code_pair: str) -> Response:
        """
        Patch exchange rate.

        Args:
            request (Request): Contains request data
            code_pair (str): path parameter indicating the currencies code pai
        Returns:
            Response: Contains data of patch exchange rate
        """
        request_serializer = UpdateExchangeRateRequestSerializer(
            data={"code_pair": code_pair, "rate": request.data["rate"]}
        )
        request_serializer.is_valid(raise_exception=True)
        dto = UpdateExchangeRateDTO(
            base_currency_code=request_serializer.data["code_pair"][0:3],
            target_currency_code=request_serializer.data["code_pair"][3:6],
            rate=request_serializer.data["rate"],
        )
        exchange_rate = ExchangeRateService.update_exchange_rate(dto)
        response_serializer = UpdateExchangeRateResponseSerializer(exchange_rate)
        return Response(response_serializer.data)
