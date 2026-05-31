from dataclasses import asdict

from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import CurrencyDto
from exchange.models import Currency
from exchange.repository import CurrencyRepository
from exchange.serializers import CurrencySerializer



class CurrenciesView(APIView):

    def get(self, request):
        currencies = CurrencyRepository.get_all()
        serializer = CurrencySerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_serializer = CurrencySerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        currency_dto = CurrencyDto(**request_serializer.validated_data)
        currency = Currency(**asdict(currency_dto))
        CurrencyRepository.create(currency)
        response_serializer = CurrencySerializer(currency)
        return Response(response_serializer.data)



