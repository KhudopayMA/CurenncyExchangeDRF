from django.urls import path

from .views import CurrenciesViewSet, CurrencyView, ExchangeRatesView


urlpatterns = [
    path("currencies", CurrenciesViewSet.as_view()),
    path("currency/<str:code>", CurrencyView.as_view()),
    path("exchangeRates", ExchangeRatesView.as_view())
]
