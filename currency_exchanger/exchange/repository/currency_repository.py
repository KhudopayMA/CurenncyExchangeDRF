from dataclasses import asdict
from typing import Optional

from django.db.models import QuerySet
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from exchange.exceptions import DatabaseOperationException
from exchange.exceptions.database_operation_exception import NotFound
from exchange.models import Currency
from exchange.dto import CurrencyDto


class CurrencyRepository:

    @staticmethod
    def get_all() -> list[Currency]:
        return list(Currency.objects.all())

    @staticmethod
    def create(data: CurrencyDto) -> Optional[Currency]:
        try:
            return Currency.objects.create(**asdict(data))
        except IntegrityError as e:
            error_msg = str(e)
            if "UNIQUE constraint failed" in error_msg:
                filed = error_msg.split(".")[-1].lower()
                raise DatabaseOperationException(
                    f"Field {filed} with value {getattr(data, filed)} already exists."
                )

    @staticmethod
    def get(**params) -> Currency:
        return Currency.objects.get(**params)
