from dataclasses import asdict

from django.db import IntegrityError
from django.db.models import QuerySet

from exchange.dto import ExchangeRateDto, RequestExchangeRateDto
from exchange.exceptions import DatabaseOperationException
from exchange.models import ExchangeRate, Currency


class ExchangeRateRepository:

    @staticmethod
    def get_all() -> QuerySet[ExchangeRate]:
        return ExchangeRate.objects.all()

    @staticmethod
    def create(data: ExchangeRateDto) -> ExchangeRate:
        try:
            return ExchangeRate.objects.create(**asdict(data))
        except IntegrityError as e:
            error_msg = str(e)
            if "UNIQUE constraint failed" in error_msg:
                filed = error_msg.split(".")[-1].lower()
                raise DatabaseOperationException(
                    f"Field {filed} with value {getattr(data, filed)} already exists."
                )