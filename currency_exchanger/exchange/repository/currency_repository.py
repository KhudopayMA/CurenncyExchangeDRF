from dataclasses import asdict

from django.db.models import QuerySet
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from exchange.exceptions import DatabaseOperationException
from exchange.models import Currency
from exchange.dto import CurrencyDto

class CurrencyRepository:

    def get_all(self) -> QuerySet[Currency]:
        return Currency.objects.all()

    def create(self, data: CurrencyDto) -> Currency:
        try:
            return Currency.objects.create(**asdict(data))
        except IntegrityError as e:
            error_msg = str(e)
            if "UNIQUE constraint failed" in error_msg:
                filed = error_msg.split(".")[-1].lower()
                raise DatabaseOperationException(
                    f"Field {filed} with value {getattr(data, filed)} already exists."
                )

    def get(self, **params) -> Currency:
        return Currency.objects.get(**params)
