from django.urls import path

from currency_exchange.views import CurrenciesView, CurrencyView, ExchangeRatesView, ExchangeRateView, ExchangeView

urlpatterns = [
    path("currencies", CurrenciesView.as_view()),
    path("currency/<str:code>", CurrencyView.as_view()),
    path("exchangeRates", ExchangeRatesView.as_view()),
    path("exchangeRate/<str:code_pair>", ExchangeRateView.as_view()),
    path("exchange", ExchangeView.as_view())
]
