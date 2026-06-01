from rest_framework.response import Response
from rest_framework.views import APIView

from exchange.dto import GetExchangeRequestDto
from exchange.serializers import GetExchangeRequestSerializer, GetExchangeResponseSerializer
from exchange.services import ExchangeService


class ExchangeView(APIView):

    def get(self, request) -> Response:
        """
        Get exchange.

        Args:
            request: Contains request data

        Returns:
            Response: Contains data of exchange

        """
        request_serializer = GetExchangeRequestSerializer(data=request.query_params)
        request_serializer.is_valid(raise_exception=True)
        dto = GetExchangeRequestDto(**request_serializer.validated_data)
        exchange_dto = ExchangeService.get_exchange(dto)
        response_serializer = GetExchangeResponseSerializer(exchange_dto)
        return Response(response_serializer.data)
