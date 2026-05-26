from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import CurrencyDto
from exchange.repository import CurrencyRepository
from exchange.serializers import CurrencySerializer



class CurrenciesView(APIView):
    serializer_class = CurrencySerializer
    currency_repository = CurrencyRepository()

    def get(self, request):
        currencies = self.currency_repository.get_all()
        serializer = self.serializer_class(currencies, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_serializer = self.serializer_class(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        currency_dto = CurrencyDto(**request_serializer.validated_data)
        currency = self.currency_repository.create(currency_dto)
        response_serializer = self.serializer_class(currency)
        return Response(response_serializer.data)



