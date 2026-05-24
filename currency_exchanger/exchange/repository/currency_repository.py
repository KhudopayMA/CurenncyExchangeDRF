from dataclasses import asdict

from django.db.models import QuerySet
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

from exchange.models import Currency
from exchange.dto import CurrencyDto

class CurrencyRepository:

    def get_all(self) -> QuerySet[Currency]:
        return Currency.objects.all()

    def create(self, data: CurrencyDto) -> Currency:
        return Currency.objects.create(**asdict(data))

    def get(self, **params) -> Currency:
        return Currency.objects.get(**params)
