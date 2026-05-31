from dataclasses import asdict
from typing import Optional

from django.db import IntegrityError
from django.db.models import QuerySet

from exchange.dto import ExchangeRateDto, GetRequestExchangeRateDto
from exchange.exceptions import DatabaseOperationException
from exchange.exceptions.database_operation_exception import NotFound
from exchange.models import ExchangeRate, Currency


class ExchangeRateRepository:

    @classmethod
    def get_all(cls) -> list[ExchangeRate]:
        return list(ExchangeRate.objects.all())

    @classmethod
    def get(cls, **params) -> Optional[ExchangeRate]:
        try:
            return ExchangeRate.objects.get(**params)
        except ExchangeRate.DoesNotExist:
            raise NotFound()

    @classmethod
    def create(cls, data: ExchangeRateDto) -> ExchangeRate:
        try:
            return ExchangeRate.objects.create(**asdict(data))
        except IntegrityError as e:
            error_msg = str(e)
            if "UNIQUE constraint failed" in error_msg:
                raise DatabaseOperationException(
                    f"Exchange rate already exists."
                )
            raise

    @classmethod
    def update(cls, data: ExchangeRateDto) -> ExchangeRate:
        exchange_rate = cls.get(base_currency_id=data.base_currency_id,
                                target_currency_id=data.target_currency_id
        )
        exchange_rate.rate=data.rate
        exchange_rate.save()
        return exchange_rate
