from django.urls import path

from exchange.views import CurrenciesView, CurrencyView, ExchangeRatesView

urlpatterns = [
    path("currencies", CurrenciesView.as_view()),
    path("currency/<str:code>", CurrencyView.as_view()),
    path("exchangeRates", ExchangeRatesView.as_view())
]
