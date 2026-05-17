from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CurrenciesViewSet, ExchangeRatesViewSet, CurrencyView

router = DefaultRouter(trailing_slash=False)
# router.register(r"currencies", CurrenciesViewSet, basename="currencies")
# router.register(r"currency", CurrencyViewSet.as_view(), basename="currency")
router.register(r"exchange_rates", ExchangeRatesViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("currencies", CurrenciesViewSet.as_view()),
    path("currency/<str:code>", CurrencyView.as_view()),
]
