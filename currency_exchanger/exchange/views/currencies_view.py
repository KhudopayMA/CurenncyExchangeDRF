from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from exchange.dto import CurrencyDto
from exchange.repository import CurrencyRepository
from exchange.serializers import CurrencySerializer

class ConflictError(APIException):
    status_code = 409


class CurrenciesView(APIView):
    serializer_class = CurrencySerializer
    currency_repository = CurrencyRepository()

    def get(self, request):
        currencies = self.currency_repository.get_currencies()
        serializer = self.serializer_class(currencies, many=True)
        return Response(serializer.data)

    def post(self, request):
        request_serializer = self.serializer_class(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        try:
            currency_dto = CurrencyDto(**request_serializer.validated_data)
            currency = self.currency_repository.create_currency(currency_dto)
            response_serializer = self.serializer_class(currency)
            return Response(response_serializer.data)
        except IntegrityError as e:
            error_msg = str(e)
            if "UNIQUE constraint failed" in error_msg:
                filed = error_msg.split(".")[-1].lower()
                return Response(
                    f"Field {filed} with value {request_serializer.validated_data.get(filed)} already exists.",
                    status=status.HTTP_409_CONFLICT,
                )
                # raise ConflictError(
                #     f"Field {filed} with value {request_serializer.validated_data.get(filed)} already exists."
                # )


