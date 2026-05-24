from dataclasses import asdict

from django.db.models import QuerySet

from exchange.dto import ExchangeRateDto, RequestExchangeRateDto
from exchange.models import ExchangeRate, Currency


class ExchangeRateRepository:

    def get_all(self) -> QuerySet[ExchangeRate]:
        return ExchangeRate.objects.all()

    def create(self, data: ExchangeRateDto) -> ExchangeRate:
        return ExchangeRate.objects.create(**asdict(data))
