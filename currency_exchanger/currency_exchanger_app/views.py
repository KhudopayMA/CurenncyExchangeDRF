from django.shortcuts import render
from rest_framework import permissions, viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Currency, ExchangeRate
from .serialyzers import CurrenciesSerializer, ExchangeRatesSerializer, CurrencySerializer


class CurrenciesViewSet(APIView):
    queryset = Currency.objects.all()
    serializer_class = CurrenciesSerializer

    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrenciesSerializer(currencies, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = CurrenciesSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CurrencyView(APIView):

    def get(self, request, code):
        # code = request.GET.get('code')
        try:
            currency = Currency.objects.get(code=code)
            serializer = CurrencySerializer(currency)
            return Response(serializer.data)
        except Currency.DoesNotExist:
            return Response(f"Currency with code {code} not found", status=status.HTTP_404_NOT_FOUND)

class ExchangeRatesViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRatesSerializer

